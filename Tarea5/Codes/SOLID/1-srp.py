class ReportGenerator:
    def generate_report(self, data):
        report = ""
        for item in data:
            report += f"Item: {item}\n"
        return report


class DataManager:
    def fetch_data(self):
        return ["Data 1", "Data 2", "Data 3"]


data_manager = DataManager()
data = data_manager.fetch_data()
report_generator = ReportGenerator()
report = report_generator.generate_report(data)
print(report)
