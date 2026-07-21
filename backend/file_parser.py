import sys
from pathlib import Path
from markitdown import MarkItDown

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
  input_file_path = Path(input_dir) / file_name

  if input_file_path.suffix not in target_formats:
    print(f"File format {input_file_path.suffix} not supported. Supported formats: {target_formats}")
    return
  try:
    result = md.convert(input_file_path)
  except Exception as e:
    print(f"Error processing file {input_file_path}: {e}")
    return
  
  output_file_path = output_path / f"{input_file_path.stem}{input_file_path.suffix}.md"
  try:
    output_file_path.write_text(result.markdown, encoding="utf-8")
    print(f"Converted {input_file_path} to {output_file_path}")
  except Exception as e:
    print(f"Error writing output file {output_file_path}: {e}")
      
if __name__ == "__main__":
  main()