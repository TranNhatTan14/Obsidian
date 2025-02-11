---
tags:
  - Work
---
# GeneStory

### KPI

- Phụ trách việc xử lý dữ liệu STR trả kết quả cho khách hàng
- Cần tham gia nhiều công việc hơn liên quan đến dự án BCA



- Mục tiêu là validate lại tool của Cúc, tìm cách để loại bỏ những điểm hete như CY

Think about the case when the input file have both reverse and forward if the variant in only 1 so skip it






# 20250210 to 20250214



# STR


- Batch cũ thì mình sẽ check lại giữa 2 tool
- passcheck
- What we want is like the sheet








- Update the code to no need to rerun again
- Update the compare result
	- Remove the mismatch sample for further analysis
- Fix bug 2025 STr
- Update code to handle well gen report
- Report Generated Successfully with 81 files in the output folder. and file not in folder is




Patients with retinopathy, nephropathy, and cardiovascular complications have significantly higher HbA1c levels compared to the non-complication group (p < 0.0001). Retinopathy also shows significantly higher HbA1c than nephropathy (p = 0.0052), while no significant differences are observed between cardiovascular vs. retinopathy or nephropathy. This suggests that poor glycemic control is strongly associated with diabetic complications, especially retinopathy.




# NSAID








- Xây dựng các UC phần mềm (còn khoảng 30)
- Hoàn thiện phân tích và viết báo NSAIDS
- Phân tích các batch STR
- Phân tích các batch mtDNA
- Dự án chọn giống heo
- Xây dựng pipeline impute

- GST và HVNN sẽ phối hợp với BAF để triển khai chọn giống heo cho BAF 
- Hiện tại BAF có full dâta cho khoảng 200k phenotype của heo và bên HVNN có sẵn vài ngàn mẫu đuôi heo trữ lạnh để làm nghiên cứu kiểu gen/kiểu hình 
- HVNN có một dự án do CP Bỉ tài trợ, chạy được khoảng 1000 mẫu với kinh phí được cấp. Tuy nhiên họ đang để cho phía Bỉ chạy wetlab và phân tích tin sinh luôn do ngại giải ngân tại VN. 
- Bên Bỉ đang chạy ILMN (iScan) nên các dữ liệu SNP sẽ khác với chạy trên chip của TFS. Mình sẽ cố thuyết phục họ chạy trên Genetitan của TFS bên đó. 
- GST và SISC và TFS sẽ tìm nguồn để tài trợ khoảng 1000-2000 mẫu cho dự án này, kèm theo việc GST sẽ chịu trách nhiệm phân tích tin sinh cho dự án để tạo lập database và pipelines. 
- Mục đích cuối cùng là tạo ra được dòng thuần gốc F0 cho đàn heo ở BAF nói riêng và VN nói chung. 
- Công nghệ chọn giống dùng microarray




Dựa trên thông tin bạn cung cấp và phân tích nội dung của Dự thảo Luật Dữ liệu và Tờ trình Dự án Luật Dữ liệu, dưới đây là các bước chiến lược để GST tận dụng cơ hội từ Luật mới:
### Nghiên cứu kỹ Dự thảo Luật Dữ liệu

- Mục tiêu: Đảm bảo sản phẩm/dịch vụ của GST đáp ứng các quy chuẩn mới, đặc biệt là liên quan đến:
	- Dữ liệu quan trọng (Điều 24) và Dữ liệu cốt lõi (Điều 25): Xác định xem sản phẩm của GST có liên quan đến các lĩnh vực được phân loại là "dữ liệu quan trọng" hay "dữ liệu cốt lõi" (như an ninh quốc gia, kinh tế, xã hội).
	- Chuẩn hóa dữ liệu (Điều 11): Đảm bảo dữ liệu của GST tuân thủ các tiêu chuẩn kỹ thuật quốc gia về kết nối, chia sẻ, đồng bộ hóa dữ liệu.
- Hành động:
	- Thành lập nhóm chuyên gia pháp lý và kỹ thuật để phân tích chi tiết Dự thảo.
	- So sánh các quy định mới với tiêu chuẩn hiện tại của GST để xác định gap cần bổ sung.

### Kiểm tra điểm mới có thể bổ sung vào Dự thảo

- Mục tiêu: Đưa voice của GST vào Dự thảo để tạo lợi thế cạnh tranh.
- Hành động:
	- Điều 6 (Hành vi bị nghiêm cấm): Đề xuất bổ sung các hành vi vi phạm liên quan đến việc "lợi dụng dữ liệu để cạnh tranh không lành mạnh" (nếu chưa có).
	- Điều 28 (Quỹ Phát triển Dữ liệu Quốc gia): Đưa GST vào danh sách đối tượng được hỗ trợ tài chính hoặc công nghệ từ Quỹ.
	- Điều 46 (Sản phẩm, dịch vụ về dữ liệu): Đảm bảo dịch vụ của GST được công nhận là "sản phẩm công nghệ cao" để hưởng ưu đãi thuế và chính sách.
### Làm việc với Bộ Y tế (BYT) và các cơ quan liên quan

- Mục tiêu: Đẩy nhanh tiến trình ban hành Luật và tạo thuận lợi cho GST.
- Hành động:
	- Bước 1: Liên hệ với Bộ Công an (đơn vị chủ trì Dự án Luật) để vào Dự thảo, đặc biệt là các liên quan đến Chương IV (Trung tâm Dữ liệu Quốc gia) và Chương V (Sản phẩm, dịch vụ về dữ liệu).
	- Bước 2: Đưa ra đề xuất chi tiết về cách GST có thể hỗ trợ triển khai Luật (ví dụ: cung cấp giải pháp công nghệ để bảo vệ dữ liệu y tế điện tử).
	- Bước 3: Tham gia các hội thảo công khai của Chính phủ để trình bày vị thế của GST như "doanh nghiệp có khả năng thay thế hàng nhập khẩu" (theo chỉ đạo của Dự thảo Luật).

### Chuẩn bị năng lực và định hướng trước khi Luật ra đời

- Mục tiêu: Đảm bảo GST sẵn sàng ngay khi Luật có hiệu lực (01/01/2026).
- Hành động:
	- Nâng cấp hệ thống: Đảm bảo cơ sở dữ liệu của GST tuân thủ tiêu chuẩn kỹ thuật quốc gia (Điều 9) và có khả năng kết nối với Trung tâm Dữ liệu Quốc gia.
	- Đào tạo nhân lực: Tạo chương trình đào tạo cho nhân viên về quản trị dữ liệu (Điều 31) và bảo vệ dữ liệu (Điều 50).
	- Định vị sản phẩm: Tập trung vào các sản phẩm/dịch vụ liên quan đến dữ liệu mở (Điều 13) và dữ liệu dùng chung (Điều 12) để phục vụ Chính phủ số.

### Khả năng tích hợp thông tin DNA vào Dự thảo Luật

- Có thể tích hợp, nhưng cần tuân thủ các quy định liên quan đến dữ liệu cá nhân nhạy cảm và bảo mật y tế. Dưới đây là các điều khoản trong Dự thảo Luật có liên quan:
	- Điều 2 (Dữ liệu cá nhân): DNA được coi là dữ liệu cá nhân nhạy cảm, do đó cần tuân thủ quy định về thu thập, lưu trữ, và sử dụng với sự đồng ý của chủ thể.
	- Điều 50 (Bảo vệ dữ liệu): Yêu cầu các cơ quan, tổ chức phải áp dụng các biện pháp bảo mật cao đối với dữ liệu cá nhân, đặc biệt là dữ liệu sinh học.
	- Điều 25 (Dữ liệu cốt lõi): Nếu DNA được phân loại là "dữ liệu cốt lõi" (ví dụ: liên quan đến an ninh quốc gia hoặc sức khỏe cộng đồng), cần tuân thủ quy trình đánh giá an toàn dữ liệu trước khi chuyển ra nước ngoài.
### Các yếu tố cần cân nhắc khi tích hợp thông tin DNA

- Vị trí của DNA trong Cơ sở dữ liệu tổng hợp quốc gia:
	- Điều 29: Cơ sở dữ liệu quốc gia về dân cư có thể bao gồm dữ liệu sinh học (DNA) nếu được quy định rõ trong danh mục dữ liệu cần thu thập.
	- Điều 31: Cần đảm bảo chất lượng dữ liệu (đúng, đủ, sạch) khi thu thập DNA, đồng thời tuân thủ quy trình xác thực và xác nhận dữ liệu.
- Vấn đề đạo đức và pháp lý:
	- Điều 6 (Hành vi bị nghiêm cấm): Tuyệt đối không được sử dụng DNA để xâm phạm quyền riêng tư, quyền tự do của cá nhân.
	- Điều 50: Đảm bảo các biện pháp bảo mật như mã hóa end-to-end, truy cập dựa trên vai trò (role-based access).

### Điều kiện cần đáp ứng để tích hợp DNA

- Điều 47 (Điều kiện cung cấp dịch vụ trung gian dữ liệu):
	- Tổ chức cung cấp dịch vụ liên quan đến DNA (ví dụ: phân tích gen) cần đáp ứng:
		- Điều kiện về cơ sở vật chất: Thiết bị y tế đạt chuẩn, hệ thống bảo mật cao.
		- Điều kiện về nhân sự: Nhân viên có chuyên môn về di truyền và bảo mật dữ liệu.
		- Điều kiện về pháp lý: Đảm bảo tuân thủ Luật Bảo vệ Dữ liệu Cá nhân (nếu có) và Luật An ninh Mạng.
- Điều 50 (Bảo vệ dữ liệu):
	- Áp dụng mã hóa dữ liệu (Điều 41) đối với thông tin DNA để đảm bảo không bị truy cập trái phép.
	- Đảm bảo quyền của chủ thể dữ liệu (ví dụ: quyền từ chối cung cấp DNA, quyền xóa dữ liệu).

### Lợi ích và rủi ro khi tích hợp DNA

- Lợi ích:
	- Y tế công cộng: Giúp chuẩn đoán sớm của các bệnh di truyền, quản lý dịch bệnh.
	- Nghiên cứu khoa học: Đưa Việt Nam vào các dự án gen toàn cầu (ví dụ: Human Genome Project).
	- Chính phủ số: Tạo nền tảng dữ liệu sinh học cho các dịch vụ công (ví dụ: giấy khai sinh điện tử).
- Rủi ro:
	- Vấn đề đạo đức: Nguy cơ phân biệt đối xử dựa trên di truyền (ví dụ: bảo hiểm từ chối bồi thường do bệnh di truyền).
	- Bảo mật: DNA là dữ liệu nhạy cảm,一một khi bị rò rỉ có thể gây tổn hại vĩnh viễn đến cá nhân.
	- Pháp lý: Hiểm họa kiện tụng từ các tổ chức quốc tế nếu vi phạm các điều ước về quyền sở hữu trí tuệ di truyền.

### Đề xuất hành động

- Đối với Bộ Công an:
	- Đưa dữ liệu sinh học (DNA) vào danh mục dữ liệu cốt lõi (Điều 25) để quản lý chặt chẽ.
	- Ban hành quy chuẩn kỹ thuật về thu thập, lưu trữ, và sử dụng DNA (tham khảo ISO/IEC 27001:2013).
- Đối với GST:
	- Đảm bảo hệ thống của mình tuân thủ tiêu chuẩn bảo mật (Điều 50) và có khả năng kết nối với Trung tâm Dữ liệu Quốc gia.
	- Đào tạo nhân viên về luật bảo vệ dữ liệu cá nhân và đạo đức di truyền



