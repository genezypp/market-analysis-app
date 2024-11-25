import csv
from fpdf import FPDF

def generate_csv_report(devices, file_path="devices_report.csv"):
    """
    Generuje raport CSV.
    """
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Model", "Condition", "Purchase Price", "Repair Cost", "Sale Price", "Margin"])
        for device in devices:
            writer.writerow([device.model, device.condition, device.purchase_price, device.repair_cost, device.sale_price, device.margin])

def generate_pdf_report(devices, file_path="devices_report.pdf"):
    """
    Generuje raport PDF.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Devices Report", ln=True, align="C")
    pdf.ln(10)

    for device in devices:
        pdf.cell(200, 10, txt=f"{device.model} - Condition: {device.condition}, Margin: {device.margin:.2f} PLN", ln=True)

    pdf.output(file_path)
