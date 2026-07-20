from pathlib import Path
from markitdown import MarkItDown
import sys

def main(
  input_dir="data_test/input",
  output_dir="data_test/output",
  target_formats=(".pdf", ".doc", ".docx", ".ppt", ".pptx", ".txt"),
):
  output_path = Path(output_dir)
  output_path.mkdir(parents=True, exist_ok=True)
  
  md = MarkItDown()
  
  if len(sys.argv) < 2:
    print("Please provide a file name as an argument.")
    return

  file_name = sys.argv[1]
  try:
    file_path = Path(input_dir) / file_name
  except Exception as e:
    print(f"Error finding file {file_name}: {e}")
    return

  if file_path.suffix in target_formats:
    try:
      md.convert(file_path)
    except Exception as e:
      print(f"Error processing file {file_name}: {e}")
      return
    
    output_file = output_path / f"{file_path.stem}.md"
    try:
      output_file.write_text(md.markdown, encoding="utf-8")
      print(f"Converted {file_name} to {output_file}")
    except Exception as e:
      print(f"Error writing output file {output_file}: {e}")
      
if __name__ == "__main__":
  main()