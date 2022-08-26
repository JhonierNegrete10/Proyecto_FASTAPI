class ProjectMarkDownsExporter:
    def __init__(self):
        self.base_docs_path = f"{__file__.replace('export_docs.py', '')}markdown/project_docs.md"

    def export_md_files_as_text(self):
        with open(self.base_docs_path, 'r') as file:
            markdown_text = file.read()
        return markdown_text

markdown_exporter = ProjectMarkDownsExporter()