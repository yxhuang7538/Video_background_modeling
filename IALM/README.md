# IALM

### 求解方法

[基于S_1_2_建模的稳健稀疏_低秩矩阵分解_饶过.pdf](IALM%2081d1ffab3273400ca228b9f3a989c683/S_1_2___.pdf)

**增广拉格朗日乘子法**

![IALM%2081d1ffab3273400ca228b9f3a989c683.jpg](IALM%2081d1ffab3273400ca228b9f3a989c683.jpg)

实际求解中只需要更新$A$或$E$各一次得到子问题的一个近似解即可，即非精确增广拉格朗日乘子法ADM。

$A_{k+1}=\arg \min _{A} L\left(A, E_{k+1}, Y_{k}, \mu_{k}\right), E_{k+1}=\arg \min _{E} L\left(A_{k+1}, E, Y_{k}, \mu_{k}\right)$

更多详细的算法内容参见下方论文的Algorithm 4、5

[The Augmented Lagrange Multiplier Method for Exact Recovery of Corrupted Low-Rank Matrices.pdf](IALM%2081d1ffab3273400ca228b9f3a989c683/1009.5055.pdf)

![IALM%2081d1ffab3273400ca228b9f3a989c683/Untitled.png](IALM%2081d1ffab3273400ca228b9f3a989c683/Untitled.png)

![IALM%2081d1ffab3273400ca228b9f3a989c683/Untitled%201.png](IALM%2081d1ffab3273400ca228b9f3a989c683/Untitled%201.png)

其中的$\langle A, B\rangle=\operatorname{tr}\left(A^{T} B\right), \quad J(Y)=\max \left(\|Y\|_{2}, \lambda^{-1}\|Y\|_{\infty}\right)$

$\mathcal{S}_{\varepsilon}[x] \doteq\left\{\begin{array}{l}x-\varepsilon, \text { if } x>\varepsilon \\x+\varepsilon, \text { if } x<-\varepsilon \\0, \quad \text { otherwise }\end{array}\right.$

$\|A\|_{F}=\sqrt{\sum_{i=1}^{m} \sum_{j=1}^{n}\left|a_{i j}\right|^{2}}$

增广拉格朗日算法中每一轮迭代最主要计算量在于奇异值分解，寻找一种高效的部分奇异值分解方法对于视频背景建模这种较大规模的问题是非常重要的。

根据算法5得到的视频结果：部分帧（从左到右依次是原始帧、背景、前景）

![IALM%2081d1ffab3273400ca228b9f3a989c683/0.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/0.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/0%201.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/0%201.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/0%202.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/0%202.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/21.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/21.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/21%201.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/21%201.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/21%202.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/21%202.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/75.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/75.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/75%201.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/75%201.bmp)

![IALM%2081d1ffab3273400ca228b9f3a989c683/75%202.bmp](IALM%2081d1ffab3273400ca228b9f3a989c683/75%202.bmp)

我的代码地址：[https://github.com/yxhuang7538/Video_background_modeling/tree/main/IALM](https://github.com/yxhuang7538/Video_background_modeling/tree/main/IALM)