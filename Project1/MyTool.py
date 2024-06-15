from crewai_tools import BaseTool
from bs4 import BeautifulSoup
# Define the custom tool
class MyTool(BaseTool):
    name: str = "Content File Adding Tool"
    description: str = "Tool to add content to a given HTML or CSS file."

    def _run(self, file_path: str, content: str) -> str:
        if file_path.endswith('.html'):
            return self._add_to_html(file_path, content)
        elif file_path.endswith('.css'):
            return self._add_to_css(file_path, content)
        else:
            return "Error: Unsupported file type. Only HTML and CSS files are supported."

    def _add_to_html(self, file_path: str, content: str) -> str:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file, 'html.parser')

            if not soup.body:
                soup.append(soup.new_tag('body'))

            new_tag = BeautifulSoup(content, 'html.parser')
            soup.body.append(new_tag)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(str(soup))

            return f"HTML file {file_path} has been modified successfully."
        except Exception as e:
            return f"Error: {str(e)}"

    def _add_to_css(self, file_path: str, content: str) -> str:
        try:
            with open(file_path, 'a', encoding='utf-8') as file:
                file.write('\n' + content)
                
            return f"CSS file {file_path} has been modified successfully."
        except Exception as e:
            return f"Error: {str(e)}"