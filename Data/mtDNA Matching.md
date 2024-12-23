---
tags:
  - GeneStory
  - Seminar
---
==How to optime the pipeline==

- Reduce checking time
- Increase accuracy

1. Open JSON
2. Open folder have abi file and open with UGENE
3. Looking for each variant in list
	1. For variant, some variant don't require to check because
		1. Signal is "good", if we know a way to confirm it is good we can reduce time to check it.

[Application of mtDNA SNP analysis in forensic casework](https://www.sciencedirect.com/science/article/abs/pii/S1872497310000232)

Vai trò của mtDNA trong nhận dạng cá thể
Tóm tắt, gợi ý hướng dẫn

Nhân tế bào
vật liệu di truyền được tổ chức thành 22 NST thường 1 NST GT


Ti thể nhà máy nl sản xuất nl, "tiền tệ"
Ti thể có bộ máy di truyền đọc lập, hệ gen ti thể (mtDNA)

Đặc điểm hệ gen ti thể 2 chuỗi mạch vòng 
- control region
- 13 gen chức năng
- 22 tRNA
- 2rRNA

Số lượng bản sao lớn, 1 ti thể có thể có nhiều hệ gen ti thể
Não cần dùng nhiều nên tế bào có nhiều ti thể?

Ti thể di truyền theo dòng mẹ
Ti thể chỉ còn lại ở tế bào trừng, 

Ti thể có một haplotype, di truyền theo haplotype

Tỉ lệ đột biến trong ti thể cao gấp 10-17 lần so với nhân
- Trong nhân có hệ thống enzym sửa chữa 
- Không có protein DNA (histone)
- Lỗi phát sinh trong quá trình tăng sinh

Vùng không mang mã nguy cơ đột biến cao nhất HV123
HV1 và HV2 cao và cao hơn HV3

Ứng dụng trong giám định dùng HV2 nhiều, HV3 mang tính bổ trợ

Tiến hành nghiên cứu, so sánh với cơ sở dữ liệu xem tỉ lệ đột biến có phù hợp không

Hai bộ dữ liệu SR2017 600 mẫu nếu tỉ lệ bắt cặp ngẫu nhiên HV1 HV2 0.7% trên dữ liệu của chúng ta 0.22%
So sánh với Hàn, Thái, Nhật Bản
Tại sao: Cỡ mẫu của chúng ta lớn hơn 600

Vai trò của mtDNA trong hình sự và tiến hóa, 
Hầu hết các mẫu là lâu đời, lâu năm 

Xương do số lượng bản sao trong mỗi ti thể lớn nhưng ta vẫn thu được mtDNA. Do đột biến cao nên rất đa dạng trên các cá thể, vì di truyền dòng mẹ
Tỉ lệ bắt cặp?
ví dụ 100 triệu dân VN có thể có hàng triệu người có bộ gen ti thể giống nhau
ở một khía cạnh nào đó có còn hơn không, khi không có thể có DNA nhân, 

Tổ chức thế giới đưa ra 1 số guide line CRF, ...       

# Q&A

mtDNA halotype là gì

Matching and Variant base
High Copy Number:
Stano;otu 
3 HV Hv1 16024 - 16365
73 340
438 

SNP
Insertopm amd Deletopm

Xanh cho thong ke
Vang cho tinh toan

MR 1:1
1. Calculate share interval
2. Compare toola based in shared interval with MR
3. IF not 
4. If mathch, extract variant
5. Claculateing mismatches
6. Compare mismatches with MR
7. Return matching results

approixmate search

Change sequence to something we can compare better like number 
Common overlap

Approximate search để co gọn lại khoảng theo sợi
Sequence realignment 
