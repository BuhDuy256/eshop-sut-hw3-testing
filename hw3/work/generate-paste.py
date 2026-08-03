import re
import os

input_file = r'C:\Users\Duy\Desktop\eshop-sut-hw3-testing\hw3\out\reports\task-1-checklist-execution\bug-reports.md'
output_file = r'C:\Users\Duy\Desktop\eshop-sut-hw3-testing\hw3\work\form-copy-paste.txt'

with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Split by bug headers
bugs = re.split(r'### F-\d{3} — .*', content)
headers = re.findall(r'### (F-\d{3} — .*)', content)

out = []
out.append('=== HƯỚNG DẪN COPY-PASTE ĐIỀN FORM TỪNG TRƯỜNG ===')
out.append('Làm theo đúng chỉ dẫn cho TỪNG CÂU HỎI của form cho mỗi lần submit.\n')

for i, header in enumerate(headers):
    bug_content = bugs[i+1]
    
    # Extract fields from the table
    screen = re.search(r'\|\s*\*\*Screen\*\*\s*\|\s*(.*?)\s*\|', bug_content)
    type_ = re.search(r'\|\s*\*\*Type\*\*\s*\|\s*(.*?)\s*\|', bug_content)
    sev = re.search(r'\|\s*\*\*Severity\*\*\s*\|\s*(.*?)\s*\|', bug_content)
    
    # Extract text sections
    steps_match = re.search(r'\*\*Steps to reproduce\*\*(.*?)\*\*Expected\*\*', bug_content, re.DOTALL)
    expected_match = re.search(r'\*\*Expected\*\*(.*?)\*\*Actual\*\*', bug_content, re.DOTALL)
    actual_match = re.search(r'\*\*Actual\*\*(.*?)\*\*Evidence\*\*', bug_content, re.DOTALL)
    fix_match = re.search(r'\*\*Suggested fix\*\*(.*?)(?:---|$)', bug_content, re.DOTALL)
    
    # Extract image
    evidence_match = re.search(r'\*\*Evidence\*\*(.*?)\*\*Suggested fix\*\*', bug_content, re.DOTALL)
    evidence_text = evidence_match.group(1).strip() if evidence_match else "Không có ảnh"
    # Clean up markdown code blocks if any
    evidence_text = evidence_text.replace('`', '')
    
    out.append(f'================ LẦN SUBMIT {i+1} ================')
    out.append(f'Bug: {header}\n')
    
    out.append('👉 Câu: Tốc độ tải trang của hệ thống như thế nào?')
    out.append('➤ Chọn: Bình thường\n')
    
    out.append('👉 Câu: Trong quá trình sử dụng, bạn có gặp lỗi nào không?')
    out.append('➤ Chọn: Có\n')
    
    out.append('👉 Câu: Nếu có, vui lòng mô tả lỗi bạn gặp phải.')
    out.append('➤ Copy và dán TẤT CẢ phần nằm giữa 2 đường cắt kéo dưới đây vào ô trả lời:')
    out.append('✂--------------------------------------------------')
    out.append(f'[BUG ID & TITLE] {header}')
    if screen: out.append(f'- Screen: {screen.group(1).strip()}')
    if type_: out.append(f'- Type: {type_.group(1).strip()}')
    if sev: out.append(f'- Severity: {sev.group(1).strip()}\n')
    
    out.append('[STEPS TO REPRODUCE]')
    if steps_match: out.append(steps_match.group(1).strip() + '\n')
    
    out.append('[EXPECTED BEHAVIOR]')
    if expected_match: out.append(expected_match.group(1).strip() + '\n')
    
    out.append('[ACTUAL RESULT]')
    if actual_match: out.append(actual_match.group(1).strip() + '\n')
    
    out.append('[SUGGESTED FIX]')
    if fix_match: out.append(fix_match.group(1).strip())
    out.append('--------------------------------------------------✂\n')
    
    out.append('👉 Câu: Hình ảnh / video lỗi mà bạn gặp phải')
    out.append(f'➤ Chọn file: {evidence_text}\n')
    
    out.append('👉 Câu: Điều bạn thích nhất ở hệ thống EMS là gì?')
    out.append('➤ Điền: N/A - Báo cáo lỗi Task 1B\n')
    
    out.append('👉 Câu: Điều gì khiến bạn chưa hài lòng khi sử dụng EMS?')
    out.append('➤ Điền: N/A - Báo cáo lỗi Task 1B\n')
    
    out.append('👉 Câu: Bạn mong muốn EMS bổ sung hoặc cải thiện tính năng nào?')
    out.append('➤ Điền: N/A - Báo cáo lỗi Task 1B\n')
    
    out.append('=> BẤM NÚT SUBMIT.\n')

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))
print(f'Successfully wrote {len(headers)} bugs to {output_file} with full field instructions')
