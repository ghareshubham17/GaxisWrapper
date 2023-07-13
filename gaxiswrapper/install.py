import frappe

def after_install():
    records = frappe.get_all("Module Onboarding")

    # Delete each record
    for record in records:
        frappe.delete_doc("Module Onboarding", record.name)
    print("end")
