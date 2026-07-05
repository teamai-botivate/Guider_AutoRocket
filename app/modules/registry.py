COMMON_MODULE = "common"

# module_key -> (display_name, aliases used for substring fallback matching against department names)
MODULES: dict[str, dict] = {
    COMMON_MODULE: {"display_name": "General / Common", "aliases": []},
    "complaint_tracker": {"display_name": "Complaint Tracker", "aliases": ["complaint", "quality"]},
    "doc_sub_manager": {"display_name": "Doc SubManager", "aliases": ["document", "subscription", "loan"]},
    "order_to_dispatch": {"display_name": "Order-to-Dispatch", "aliases": ["dispatch", "logistics"]},
    "lead_to_order": {"display_name": "Lead-to-Order", "aliases": ["sales", "lead", "enquiry"]},
    "hrfms": {"display_name": "HRFMS", "aliases": ["hr", "humanresources", "payroll"]},
    "mis": {"display_name": "MIS", "aliases": ["mis", "performance"]},
    "maintenance": {"display_name": "Maintenance", "aliases": ["maintenance", "workorder"]},
    "petty_cash": {"display_name": "Petty Cash", "aliases": ["pettycash", "cash"]},
    "financial": {"display_name": "Financial", "aliases": ["finance", "accounts", "accounting"]},
    "purchase_sfms_indent": {"display_name": "Purchase / SFMS Indent", "aliases": ["purchase", "procurement", "indent", "sfms", "storefms"]},
    "production_planning": {"display_name": "Production Planning", "aliases": ["production"]},
    "training": {"display_name": "Training", "aliases": ["training"]},
    "repair": {"display_name": "Repair", "aliases": ["repair"]},
    "asset_management": {"display_name": "Asset Management", "aliases": ["asset"]},
    "workflow_builder": {"display_name": "Workflow Builder", "aliases": ["workflow"]},
    "payment_workflow": {"display_name": "Payment Workflow", "aliases": ["payment"]},
    "mom_system": {"display_name": "MOM System", "aliases": ["mom", "meeting"]},
    "checklist_delegation": {"display_name": "Checklist & Delegation", "aliases": ["checklist", "delegation"]},
}


def is_valid_module(module_key: str) -> bool:
    return module_key in MODULES


def display_name(module_key: str | None) -> str:
    if module_key is None:
        return "that module"
    entry = MODULES.get(module_key)
    return entry["display_name"] if entry else module_key


def all_module_keys() -> list[str]:
    return list(MODULES.keys())


def non_common_module_keys() -> list[str]:
    return [key for key in MODULES if key != COMMON_MODULE]


def aliases_for(module_key: str) -> list[str]:
    entry = MODULES.get(module_key)
    return entry["aliases"] if entry else []
