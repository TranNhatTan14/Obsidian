---
tags:
  - Research
  - Paper
  - Hybrid
links:
  - "[[Identify of bacterial plasmid with assembly graph using Graph Transformer]]"
aliases:
  - "PLASMe: a tool to identify PLASMid contigs from short-read assemblies using transformer"
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10450166/pdf/gkad578.pdf
---
- Thay vì chỉ tập trung vào đặc điểm plasmid có (gene, protein tren do), tap trung them vao nhung gen co trong bacterial ma khong co trong plasmid (như là hình của biểu đồ ven)
- Cho loài mới khi chưa có dữ liệu để training, chưa có dữ liệu để align
- Cảm giác giống như bài toán Go khi có nhiều nước đi mới mà máy tính thực hiện mà con người chưa tỉm ra

- Plasmid have a large diversity, novel plasmids may contain proteins that cannot be aligned with the current database, leading to inaccurate predictions. ==Something like Auto Tokenize==
	- If a contig only contain new proteins that cannot be aligned to the database, it poses a difficult case for most tools (PLASMe and alignment-based tools)
		- Deeplasmid also relies on alignment based features such as those from HM-MER, without alignmnent length and the number of contained genes, learning to inaccurate predictions
		- Tools that rely on motifs or k-mer frequeccy, such as PPR-Meta can only predict accurately if the sequence contain specific motifs or k-mer frequency distribution that have been seen before 
	- Plasmids contain "unseen" proteins that can still be aligned with known ones. PLASMe can still accurately classify these contigs as long as they possess know essential proteins. Howerver, alignme based tools may classigy these contigs as chromosome due to the poor alignment. For example, Deeplasmid may not construc Pfam vector correct for these novel protein, jeopardizing its overral performance. ==To improve the model'sensitivity, besides updating and expanding the database in time, we will dig deeper into the relationship between plasmid proteins to buld a bridge between known and unknown tokens==
- The current tokens contains only proteins of plasmid. Studies have show that protein critical for bacterial survival are more likely to be found in chromosme. Therefore adding protein specific to chromosme may help further improve the learning model accuracy. We will add the essential chromosome proterin to the current prootein databse to improve precision further
- The interpretation of Transformer identified potentially unannotated PCs that may also play an important role tin the life of plasmid. Predicting the dunction of these unaootated pplasmid protein may help study the evelotionary as well as ecological significance of plasmid
- Mô phỏng lại bộ gene hoàn chỉnh của vi khuẩn (Đoạn CHR or PLM đúng ra thì phải có 2 mạch, tìm vế tương ứng để sửa những điểm sai)
- Tìm ra các gene đặc thù cho vi khuẩn bằng cách tokenize từ Transformer

The Transformer identified more plasmid than BLAST
The top 3 tools are all ==hybrid method== that combine machine learning and features derived from protein alignment 

Combining deep learning and homology search to identify plasmids in short-read assemblies.
==Identify what is plasmid and what is NOT plasmid (chromosome)==
Contigs that are highly similar to known  plasmid are directly classified as plasmid. Inputs that share somewhat similarities are examined by the deep learning component in PLASME
Construct the plasmid protein clusters as vocabulary and then used Transformer to learn the important of proteins and correlation between them
By interpreting Transformer, we found that the more important tokens for identifying plasmids were associated with plasmid were associated with plasmid core genes.
Overall, PLASME can quickly and accurately identify plasmids in assembled contigs

Short contigs tend to contain more false positives. Due to thte horizontal gene transfer between chromosomes and plasmid, identifying plasmid from short sequeces may result in false positive. Thus, idnetifying the fragment plasmid sequences remain a challenging task
PLASMe had the best performance on identifying short plasmid.
PLASMe will output the identified plasmids with marking the starting and ending position in an input sequence if it can be aligned to chromosomal genomes with high similarity
==User can use our prediction and the marked region to further screen false positive using their domain knowledge about the data/sample.==

PC-level token is better at learning the importance of different proteins and the relationship between them
==This use PC-level, I think we don't use PC instead we use protein unique for plasmid and chromosome==

For longer sequences. using protein as tokens and embedding them into vectors result in much shorter vectors than those generated by k-mer or BPE
Using shorter input vectors can reduce the model complexity which helps model trianing on a GPU
However PC-clustering tokenization also help some limiatation as it is more prone to OOV isssues. Therefore, for newer plasmid, using PC tokens may lead to false negatives