"""Decision-evaluation logic. Python validates model scores and computes the final total."""
from __future__ import annotations

from typing import Any

RUBRIC = {
    "evidence_support": {
        "label": "Uses relevant released evidence", "max": 25,
        "hint": "Cite records that directly support each material claim; distinguish source claims from corroborated facts.",
    },
    "counterevidence": {
        "label": "Addresses counterevidence and conflicts", "max": 20,
        "hint": "Address the supplier dispatch claim, carrier status, warehouse count, and address-change ambiguity.",
    },
    "uncertainty": {
        "label": "Calibrates uncertainty fairly", "max": 20,
        "hint": "State what is and is not established; do not infer theft, fraud, or responsibility without corroboration.",
    },
    "next_action": {
        "label": "Chooses a useful next investigative step", "max": 20,
        "hint": "Name a specific record or verification step and explain which uncertainty it would resolve.",
    },
    "traceability": {
        "label": "Valid evidence IDs and source traceability", "max": 15,
        "hint": "Use only evidence IDs currently released in this session and connect them to claims.",
    },
}


def deterministic_score(
    conclusion: str, support_ids: list[str], counter_ids: list[str], confidence: int,
    next_action: str, rationale: str, visible_evidence: list[dict[str, Any]],
) -> dict[str, Any]:
    """Transparent fallback rubric; intentionally conservative and not an expert judgment."""
    visible = {e["id"]: e for e in visible_evidence}
    valid_support = list(dict.fromkeys(i for i in support_ids if i in visible))
    valid_counter = list(dict.fromkeys(i for i in counter_ids if i in visible))
    invalid = sorted(set(i for i in support_ids + counter_ids if i not in visible))
    all_text = (conclusion + " " + rationale + " " + next_action).lower()
    cited_text = "\n".join(visible[i]["text"].lower() for i in set(valid_support + valid_counter))

    # Evidence-support score: requires released citations plus concrete case facts.
    support_score = min(15, len(valid_support) * 5)
    fact_checks = [
        any(t in all_text for t in ["500", "full order", "order quantity"]),
        any(t in all_text for t in ["420", "warehouse count", "receiving count", "shortfall"]),
        any(t in all_text for t in ["tracking", "delivery status", "delivery scan"]),
        any(t in all_text for t in ["address change", "address-change", "authorization", "approval"]),
        bool(valid_support) and any(visible[i]["source"].lower() in cited_text for i in valid_support),
    ]
    support_score += sum(fact_checks) * 2
    support_score = min(25, support_score)

    # Counterevidence: IDs selected in the counterevidence field and issues explicitly discussed.
    counter_score = min(12, len(valid_counter) * 4)
    counter_topics = [
        any(t in all_text for t in ["supplier", "dispatch", "packing slip"]),
        any(t in all_text for t in ["carrier", "tracking", "delivery status"]),
        any(t in all_text for t in ["warehouse", "420", "count"]),
        any(t in all_text for t in ["address", "authorization", "approval"]),
    ]
    counter_score += min(8, sum(counter_topics) * 2)

    uncertainty_phrases = [
        "cannot conclude", "not enough evidence", "insufficient evidence", "unresolved",
        "not established", "does not prove", "not independently verified", "cannot determine",
        "not yet established", "no firm conclusion", "uncertain",
    ]
    uncertainty_score = min(16, sum(phrase in all_text for phrase in uncertainty_phrases) * 4)
    if 20 <= confidence <= 80:
        uncertainty_score += 4
    if confidence >= 90 and not any(p in all_text for p in uncertainty_phrases):
        uncertainty_score = max(0, uncertainty_score - 4)
    uncertainty_score = min(20, uncertainty_score)

    action_text = next_action.lower()
    action_checks = [
        any(t in action_text for t in ["request", "obtain", "retrieve"]),
        any(t in action_text for t in ["proof of delivery", "pod", "packing", "handover", "weight", "audit log", "count sheet", "receiving log", "recount", "authorization"]),
        any(t in action_text for t in ["verify", "compare", "reconcile", "confirm", "inspect", "preserve", "authenticate"]),
        len(next_action.strip()) >= 45,
    ]
    action_score = min(20, sum(action_checks) * 5)

    trace_score = min(15, len(set(valid_support + valid_counter)) * 5)
    if invalid:
        trace_score = max(0, trace_score - min(15, 5 * len(invalid)))

    scores = {
        "evidence_support": support_score,
        "counterevidence": counter_score,
        "uncertainty": uncertainty_score,
        "next_action": action_score,
        "traceability": trace_score,
    }
    feedback = []
    for key, item in RUBRIC.items():
        earned = scores[key]
        feedback.append({
            "criterion": item["label"], "earned": earned, "max": item["max"],
            "feedback": "Good coverage under the deterministic fallback rubric." if earned >= item["max"] * .75 else item["hint"],
        })
    if invalid:
        feedback.append({"criterion": "Invalid evidence references", "earned": 0, "max": 0,
                         "feedback": "Unavailable or unreleased IDs were not accepted: " + ", ".join(invalid)})
    return {"total": sum(scores.values()), "scores": scores, "feedback": feedback,
            "valid_support": valid_support, "valid_counter": valid_counter, "invalid_ids": invalid,
            "evaluation_mode": "deterministic fallback (heuristic; review manually)"}


def validate_model_evaluation(
    proposed: dict[str, Any], support_ids: list[str], counter_ids: list[str],
    visible_evidence: list[dict[str, Any]],
) -> dict[str, Any]:
    """Validate structured model criterion scores; Python computes the final total."""
    visible = {e["id"]: e for e in visible_evidence}
    expected = set(RUBRIC)
    criteria = proposed.get("criteria")
    if not isinstance(criteria, dict) or set(criteria) != expected:
        raise ValueError("Model evaluation did not return exactly the required rubric criteria.")
    scores: dict[str, int] = {}
    feedback: list[dict[str, Any]] = []
    for key, spec in RUBRIC.items():
        item = criteria[key]
        if not isinstance(item, dict) or type(item.get("score")) is not int:
            raise ValueError(f"Invalid score type for {key}.")
        if not 0 <= item["score"] <= spec["max"]:
            raise ValueError(f"Score for {key} is outside its allowed range.")
        if not isinstance(item.get("feedback"), str) or not item["feedback"].strip():
            raise ValueError(f"Missing feedback for {key}.")
        accepted_score = item["score"]
        # Deterministic evidence-presence guardrails prevent generous LLM scores
        # where the submission omitted the relevant evidence selections.
        if key == "evidence_support" and not support_ids:
            accepted_score = min(accepted_score, 5)
        elif key == "counterevidence" and not counter_ids:
            accepted_score = min(accepted_score, 5)
        elif key == "traceability":
            valid_unique = len(set(support_ids + counter_ids) & set(visible))
            accepted_score = min(accepted_score, min(spec["max"], valid_unique * 5))
        scores[key] = accepted_score
        note = item["feedback"].strip()[:1000]
        if accepted_score < item["score"]:
            note += " Python applied an evidence-presence cap because the submission did not select enough valid evidence IDs for this criterion."
        feedback.append({"criterion": spec["label"], "earned": accepted_score, "max": spec["max"],
                         "feedback": note})
    model_ids = proposed.get("referenced_evidence_ids", [])
    if not isinstance(model_ids, list) or any(not isinstance(x, str) for x in model_ids):
        raise ValueError("Model evidence references are malformed.")
    invalid_model_ids = sorted(set(model_ids) - set(visible))
    if invalid_model_ids:
        raise ValueError("Model referenced unavailable or unreleased evidence IDs: " + ", ".join(invalid_model_ids))
    selected_ids = list(dict.fromkeys(support_ids + counter_ids))
    invalid_selected = sorted(set(selected_ids) - set(visible))
    if invalid_selected:
        raise ValueError("Submission contains unavailable or unreleased evidence IDs.")
    return {
        "total": sum(scores.values()), "scores": scores, "feedback": feedback,
        "valid_support": list(dict.fromkeys(support_ids)), "valid_counter": list(dict.fromkeys(counter_ids)),
        "invalid_ids": [], "evaluation_mode": "LLM-assisted criterion evaluation; Python validated ranges and calculated total",
    }
