
import textract
text = textract.process("/Users/vanshkumarsingh/Downloads/resume_parser/Srikanth_SrDataEngineer - Copy.doc")
print(text.decode('utf-8'))