# Assignment2 - Problem1-3

[TOC]

## Problem1

In the augmented Euclidean plane, there is a line $x-3y+4=0$, what is the homogeneous coordinate of the infinity point of this line?

### Solution

On the augmented Euclidean plane, a line and infinity intersect at infinity.

That means we have to calculate the intersection of this line and the infinite line.

Let the line $l:x-3y+4=0$, we can easily conclude that the homogeneous coordinate of the line $l$ is $(1,-3,4)$.

The homogeneous coordinates of the infinity line $l_{\infin}$ is $(0,0,1)$.

So the homogeneous coordinates of the intersection of these two straight lines is:

​		$l \times l_{\infin}=(1,-3,4)\times(0,0,1)=(\begin{bmatrix} -3&4\\0&1\\ \end{bmatrix},-\begin{bmatrix} 1&4\\0&1\\ \end{bmatrix},\begin{bmatrix} 1&-3\\0&0\\ \end{bmatrix})=(-3,-1,0)$

Therefore, the homogeneous coordinates of the infinite point of the line $l:x-3y+4=0$ are $k(-3,-1,0)^{T}$and $k \neq 0$.

## Problem2

For performing nonlinear optimization in the pipeline of camera calibration, we need to compute the Jacobian matrix of $\bold p_{d} $ w.r.t $ \bold p_{n}$, i.e., $\frac{d\bold {p}_d}{d\bold {p}_n^T}$.

It should be noted that in this question $\bold p_{d} $ is the function of $ \bold p_{n}$ and all the other parameters can be regarded as 

constants. 

### Solution

We know that:

​										$\bold p_{d}=(x_d,y_d)^T,\bold p_{n}=(x_n,y_n)^T$
$$
\left\{  
             \begin{array}{lr}  
             x_d=x_n(1+k_1r^2+k_2r^4)+2\rho_1x_ny_n+\rho_2(r^2+2x_n^2)+x_nk_3r^6  \\  
             y_d=y_n(1+k_1r^2+k_2r^4)+2\rho_2x_ny_n+\rho_1(r^2+2y_n^2)+y_nk_3r^6\\  
              
             \end{array}  
\right.
\\
where \ r^2=x_n^2+y_n^2
$$

$$
\frac{d\bold {p}_d}{d\bold {p}_n^T}=\begin{bmatrix}\frac{\partial x_d}{\partial x_n}&\frac{\partial x_d}{\partial y_n} \\\frac{\partial y_d}{\partial x_n}&\frac{\partial y_d}{\partial y_n}\end{bmatrix}
$$

First, we should know that:
$$
\frac{\partial r}{\partial x_n}=x_n(x_n^2+y_n^2)^{-\frac{1}{2}}=x_nr^{-1}\\\frac{\partial r}{\partial y_n}=y_n(x_n^2+y_n^2)^{-\frac{1}{2}}=y_nr^{-1}
$$
Next, I will calculate the four formulas: $\frac{\partial x_d}{\partial x_n},\frac{\partial x_d}{\partial y_n},\frac{\partial y_d}{\partial x_n},\frac{\partial y_d}{\partial y_n}$one by one: 

Caculate $\frac{\partial x_d}{\partial x_n}:$
$$
\frac{\partial x_d}{\partial x_n}=(1+k_1r^2+k_2r^4)+x_n(2k_1r\frac{\partial r}{\partial x_n}+4k_2r^3\frac{\partial r}{\partial x_n})+2\rho_1y_n+\rho_2(2r\frac{\partial r}{\partial x_n}+4x_n)+k_3r^6+6x_nk_3r^5\frac{\partial r}{\partial x_n}\\=(1+k_1r^2+k_2r^4)+x_n(2k_1x_n+4k_2r^2x_n)+2\rho_1y_n+\rho_2(2x_n+4x_n)+k_3r^6+x_n(6k_3r^4x_n)\\
=(2k_1+4k_2r^2+6k_3r^4)x_n^2+6\rho_2x_n+2\rho_1y_n+1+k_1r^2+k_2r^4+k_3r^6
$$
Caculate $\frac{\partial x_d}{\partial y_n}:$
$$
\frac{\partial x_d}{\partial y_n}=x_n(2k_1r\frac{\partial r}{\partial y_n}+4k_2r^3\frac{\partial r}{\partial y_n})+2\rho_1x_n+2\rho_2r\frac{\partial r}{\partial y_n}+6x_nk_3r^5\frac{\partial r}{\partial y_n}\\=x_n(2k_1y_n+4k_2r^2y_n)+2\rho_1x_n+2\rho_2y_n+6k_3r^4x_ny_n\\=(2k_1+4k_2r^2+6k_3r^4)x_ny_n+2\rho_1x_n+2\rho_2y_n
$$
Caculate $\frac{\partial y_d}{\partial x_n}:$
$$
\frac{\partial y_d}{\partial x_n}=y_n(2k_1r\frac{\partial r}{\partial x_n}+4k_2r^3\frac{\partial r}{\partial x_n})+2\rho_2y_n+2\rho_1r\frac{\partial r}{\partial x_n}+6y_nk_3r^5\frac{\partial r}{\partial x_n}\\=(2k_1+4k_2r^2+6k_3r^4)x_ny_n+2\rho_1x_n+2\rho_2y_n
$$
Caculate $\frac{\partial y_d}{\partial y_n}:$
$$
\frac{\partial y_d}{\partial y_n}=(1+k_1r^2+k_2r^4)+y_n(2k_1r\frac{\partial r}{\partial y_n}+4k_2r^3\frac{\partial r}{\partial y_n})+2\rho_2x_n+\rho_1(2r\frac{\partial r}{\partial y_n}+4y_n)+k_3r^6+6y_nk_3r^5\frac{\partial r}{\partial y_n}\\=(1+k_1r^2+k_2r^4)+x_n(2k_1x_n+4k_2r^2x_n)+2\rho_1y_n+\rho_2(2x_n+4x_n)+k_3r^6+x_n(6k_3r^4x_n)\\
=(2k_1+4k_2r^2+6k_3r^4)y_n^2+6\rho_1y_n+2\rho_2x_n+1+k_1r^2+k_2r^4+k_3r^6
$$
So the Jacobian matrix is:
$$
\frac{d\bold {p}_d}{d\bold {p}_n^T}=\begin{bmatrix}\frac{\partial x_d}{\partial x_n}&\frac{\partial x_d}{\partial y_n} \\\frac{\partial y_d}{\partial x_n}&\frac{\partial y_d}{\partial y_n}\end{bmatrix}\\=\begin{bmatrix}(2k_1+4k_2r^2+6k_3r^4)x_n^2+6\rho_2x_n+2\rho_1y_n+1+k_1r^2+k_2r^4+k_3r^6&(2k_1+4k_2r^2+6k_3r^4)x_ny_n+2\rho_1x_n+2\rho_2y_n \\(2k_1+4k_2r^2+6k_3r^4)x_ny_n+2\rho_1x_n+2\rho_2y_n&(2k_1+4k_2r^2+6k_3r^4)y_n^2+6\rho_1y_n+2\rho_2x_n+1+k_1r^2+k_2r^4+k_3r^6\end{bmatrix}
$$

## Problem3

Please give the concrete form of Jacobian matrix of $\bold r$ w.r.t $\bold d$, i.e.,$\frac{d\bold r}{d\bold {d}^T}\in R^{9 \times 3}$.

In order to make it easy to check your result, please follow the following notation requirements, 

$ \alpha \overset{\triangle}{=}sin\theta, \beta\overset{\triangle}{=}cos\theta, \gamma\overset{\triangle}{=}1-cos\theta $

In other words, the ingredients appearing in your formula are restricted to $\alpha, \beta, \gamma,\theta,n_1,n_2,n_3.$

### Solution

$\bold n=[n_1\ n_2\ n_3]^T,\bold n=[n_1\ n_2\ n_3],$so $\bold {nn}^T=\begin{bmatrix} n_1n_1 & n_1n_2 & n_1n_3 \\ n_2n_1 & n_2n_2 & n_2n_3 \\ n_3n_1 & n_3n_2 & n_3n_3 \end{bmatrix}$,$\bold n$^$=\begin{bmatrix}0 &-n_3& n_2 \\n_3&0&-n_1\\-n_2& n_1&0\end{bmatrix}$ .

According to the Rodriguez formula, we can conclude that:
$$
\bold{R}=\begin{bmatrix}\cos{\theta} & &\\  &\cos{\theta}& \\ & &\cos{\theta}\end{bmatrix}+(1-\cos{\theta})\begin{bmatrix}n_1n_1 &n_1n_2 &n_1n_3\\ n_2n_1 &n_2n_2& n_2n_3\\n_3n_1 & n_3n_2&n_3n_3\end{bmatrix}+\sin{\theta}\begin{bmatrix}0 &-n_3 &n_2\\n_3& 0&-n_1\\ -n_2& n_1&0\end{bmatrix}\\
=\begin{bmatrix}\beta & &\\  &\beta& \\ & &\beta\end{bmatrix}+\gamma\begin{bmatrix}n_1n_1 &n_1n_2 &n_1n_3\\ n_2n_1 &n_2n_2& n_2n_3\\n_3n_1 & n_3n_2&n_3n_3\end{bmatrix}+\alpha\begin{bmatrix}0 &-n_3 &n_2\\n_3& 0&-n_1\\ -n_2& n_1&0\end{bmatrix}\\
=\begin{bmatrix}\beta+\gamma n_1^2 &\gamma n_1n_2-\alpha n_3&\gamma n_1n_3+\alpha n_2 \\ \gamma n_1n_2 +\alpha n_3&\beta+\gamma n_2^2& \gamma n_2n_3-\alpha n_1\\ \gamma n_1n_3-\alpha n_2&\gamma n_2n_3 +\alpha n_1 &\beta+\gamma n_3^2\end{bmatrix}
$$
So we can get $\bold r:$									
$$
\bold r=\begin {bmatrix} \beta+\gamma n_1^2\\\gamma n_1n_2-\alpha n_3\\\gamma n_1n_3+\alpha n_2\\\gamma n_1n_2 +\alpha n_3\\\beta+\gamma n_2^2\\\gamma n_2n_3-\alpha n_1\\\gamma n_1n_3-\alpha n_2\\\gamma n_2n_3 +\alpha n_1\\\beta+\gamma n_3^2\end{bmatrix}
$$
According to the relationship between $\bold d,\theta$ and $\bold n:$ $\bold d=\begin {bmatrix}d_1\\d_2\\d_3\end {bmatrix}=\theta\bold n=\theta\begin {bmatrix}n_1\\n_2\\n_3\end {bmatrix}$.

Beacause $\bold n$ is a unit vector, we have $\theta=||\bold d||_2=\sqrt{d_1^2+d_2^2+d_3^2}$ .

Since the required derivative contains $\theta$ term, so here's a unified calculation:
$$
\frac{\partial \theta}{\partial d_i}=\frac{d_i}{\sqrt{d_1^2+d_2^2+d_3^2}}=\frac{d_i}{\theta}=n_i\\
\frac{\partial \alpha}{\partial d_i}=\frac{\partial sin\theta}{\partial d_i}=cos\theta\frac{\partial \theta}{\partial d_i}=\beta n_i\\
\frac{\partial \beta}{\partial d_i}=\frac{\partial cos\theta}{\partial d_i}=-sin\theta\frac{\partial \theta}{\partial d_i}=-\alpha n_i\\
\frac{\partial \gamma}{\partial d_i}=\frac{\partial (1-cos\theta)}{\partial d_i}=sin\theta\frac{\partial \theta}{\partial d_i}=\alpha n_i
$$
Since the required derivative contains $n_i$ term, so here's a unified calculation:
$$
According\ to  \ the \ relationship\  between\ \bold d,\theta  \ and\  \bold n:\\
n_i=\frac{d_i}{\theta}=\frac{d_i}{\sqrt{d_1^2+d_2^2+d_3^2}}\\
\frac{\partial n_i}{\partial d_i}=\frac{{\sqrt{d_1^2+d_2^2+d_3^2}}-d_i\frac{d_i}{\sqrt{d_1^2+d_2^2+d_3^2}}}{d_1^2+d_2^2+d_3^2}=\frac{1-\frac{{d_i}^2}{{d_1^2+d_2^2+d_3^2}}}{\sqrt{d_1^2+d_2^2+d_3^2}}=\frac{1-n_i^2}{\theta}\\
\frac{\partial n_i}{\partial d_j}=\frac{-d_i\frac{d_j}{\sqrt{d_1^2+d_2^2+d_3^2}}}{d_1^2+d_2^2+d_3^2}=-\frac{n_in_j}{\theta},i \neq j
$$
The Jacobian matrix is :
$$
\frac{d\bold r}{d\bold {d}^T}=\begin{bmatrix}\frac{\partial r_{11}}{\partial d_1}&\frac{\partial r_{11}}{\partial d_2}&\frac{\partial r_{11}}{\partial d_3}\\\frac{\partial r_{12}}{\partial d_1}&\frac{\partial r_{12}}{\partial d_2}&\frac{\partial r_{12}}{\partial d_3}\\\vdots&\vdots&\vdots\\\frac{\partial r_{33}}{\partial d_1}&\frac{\partial r_{33}}{\partial d_2}&\frac{\partial r_{33}}{\partial d_3}\end{bmatrix}
$$
I then found that the derivative of this matrix is very complex, but can observe that some classes of $r_{ij}$ have similar formula substructures, so I can calculate them roughly first:

Equations like structures like $\beta+\gamma n_i^2(r_{11},r_{22},r_{33}):$
$$
\frac{\partial {(\beta+\gamma n_i^2)}}{\partial d_i}=\frac{\partial {\beta}}{\partial d_i}+\frac{\partial {(\gamma n_i^2)}}{\partial d_i}=-\alpha n_i+\alpha n_in_i^2+2\gamma n_i \frac {1-n_i^2}{\theta}\\=\alpha n_i(n_i^2-1)+\frac{2\gamma n_i(1-n_i^2)}{\theta}\\
\frac{\partial {(\beta+\gamma n_i^2)}}{\partial d_j}=\frac{\partial {\beta}}{\partial d_j}+\frac{\partial {(\gamma n_i^2)}}{\partial d_j}=-\alpha n_j +\alpha n_jn_i^2-2\gamma n_i\frac{n_in_j}{\theta}\\=an_j(n_i^2-1)-\frac{2\gamma n_i^2n_j}{\theta},where \ i\neq j
$$
Equations like structures like $\gamma n_jn_k\pm \alpha n_i(r_{12},r_{13},r_{21},r_{23},r_{31},r_{32}):$
$$
\frac{\partial ({\gamma n_jn_k \pm \alpha n_i})}{\partial d_i}=\frac{\partial ({\gamma n_jn_k })}{\partial d_i}+\frac{\partial ({ \pm \alpha n_i})}{\partial d_i}\\=\alpha n_in_jn_k-\gamma \frac{n_in_j}{\theta}n_k-\gamma \frac{n_in_k}{\theta}n_{j}\pm \beta n_i^2 \pm \alpha \frac{1-n_i^2}{\theta}\\=n_i(\alpha n_jn_k \pm \beta n_i)+\frac{\pm \alpha(1-n_i^2)-2\gamma n_in_jn_k}{\theta}
$$

$$
\frac{\partial ({\gamma n_jn_k \pm \alpha n_i})}{\partial d_j}=\frac{\partial ({\gamma n_jn_k })}{\partial d_j}+\frac{\partial ({ \pm \alpha n_i})}{\partial d_j}\\=\alpha n_j^2n_k+\gamma \frac{1-n_j^2}{\theta}n_k-\gamma n_j\frac{n_jn_k}{\theta}\pm \beta n_in_j\mp\alpha\frac{n_in_j}{\theta}\\=n_j(\alpha n_jn_k\pm \beta n_i)+\frac{\gamma n_k(1-2n_j^2)\mp \alpha n_in_j}{\theta},where\ i \neq j
$$

So we can finally sort it out:

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{11}}{\partial d_1}=\frac{\partial (\beta+\gamma n_1^2)}{\partial d_1}=\frac{2\gamma n_1(1-n_1^2)}{\theta}+\alpha n_1(n_1^2-1)
$$

$$
\frac{\partial r_{11}}{\partial d_2}=\frac{\partial (\beta+\gamma n_1^2)}{\partial d_2}=-\frac{2\gamma n_1^2n_2}{\theta}+\alpha n_2(n_1^2-1)
$$

$$
\frac{\partial r_{11}}{\partial d_3}=\frac{\partial (\beta+\gamma n_1^2)}{\partial d_3}=-\frac{2\gamma n_1^2n_3}{\theta}+\alpha n_3(n_1^2-1)
$$ { }

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{12}}{\partial d_1}=\frac{\partial (\gamma n_1n_2-\alpha n_3)}{\partial d_1}=n_1(\alpha n_1n_2-\beta n_3)+\frac{\gamma n_2(1-2n_1^2)+\alpha n_1n_3}{\theta}
$$

$$
\frac{\partial r_{12}}{\partial d_2}=\frac{\partial (\gamma n_1n_2-\alpha n_3)}{\partial d_2}=n_2(\alpha n_1n_2-\beta n_3)+\frac{\gamma n_1(1-2n_2^2)+\alpha n_2n_3}{\theta}
$$

$$
\frac{\partial r_{12}}{\partial d_3}=\frac{\partial (\gamma n_1n_2-\alpha n_3)}{\partial d_3}=n_3(\alpha n_1n_2-\beta n_3)+\frac{\alpha (n_3^2-1)-2\gamma n_1n_2n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{13}}{\partial d_1}=\frac{\partial (\gamma n_1n_3+\alpha n_2)}{\partial d_1}=n_1(\alpha n_1n_3+\beta n_2)+\frac{\gamma n_3(1-2n_1^2)-\alpha n_1n_2}{\theta}
$$

$$
\frac{\partial r_{13}}{\partial d_2}=\frac{\partial (\gamma n_1n_3+\alpha n_2)}{\partial d_2}=n_2(\alpha n_1n_3+\beta n_2)+\frac{\alpha(1-n_2^2)-2\gamma n_1n_2n_3}{\theta}
$$

$$
\frac{\partial r_{13}}{\partial d_3}=\frac{\partial (\gamma n_1n_3+\alpha n_2)}{\partial d_3}=n_3(\alpha n_1n_3+\beta n_2)+\frac{\gamma n_1(1-2n_3^2)-\alpha n_2n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{21}}{\partial d_1}=\frac{\partial (\gamma n_1n_2+\alpha n_3)}{\partial d_1}=n_1(\alpha n_1n_2+\beta n_3)+\frac{\gamma n_2(1-2n_1^2)-\alpha n_1n_3}{\theta}
$$

$$
\frac{\partial r_{21}}{\partial d_2}=\frac{\partial (\gamma n_1n_2+\alpha n_3)}{\partial d_2}=n_2(\alpha n_1n_2+\beta n_3)+\frac{\gamma n_1(1-2n_2^2)-\alpha n_2n_3}{\theta}
$$

$$
\frac{\partial r_{21}}{\partial d_3}=\frac{\partial (\gamma n_1n_2+\alpha n_3)}{\partial d_3}=n_3(\alpha n_1n_2+\beta n_3)+\frac{\alpha(1-n_3^2)-2\gamma n_1n_2n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{22}}{\partial d_1}=\frac{\partial (\beta+\gamma n_2^2)}{\partial d_1}=-\frac{2\gamma n_1n_2^2}{\theta}+\alpha n_1(n_2^2-1)
$$

$$
\frac{\partial r_{22}}{\partial d_2}=\frac{\partial (\beta+\gamma n_2^2)}{\partial d_2}=\frac{2\gamma n_2(1-n_2^2)}{\theta}+\alpha n_2(n_2^2-1)
$$

$$
\frac{\partial r_{22}}{\partial d_3}=\frac{\partial (\beta+\gamma n_2^2)}{\partial d_3}=-\frac{2\gamma n_2^2n_3}{\theta}+\alpha n_3(n_2^2-1)
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{23}}{\partial d_1}=\frac{\partial (\gamma n_2n_3-\alpha n_1)}{\partial d_1}=n_1(\alpha n_2n_3-\beta n_1)-\frac{\alpha(1-n_1^2)+2\gamma n_1n_2n_3}{\theta}
$$

$$
\frac{\partial r_{23}}{\partial d_2}=\frac{\partial (\gamma n_2n_3-\alpha n_1)}{\partial d_2}=n_2(\alpha n_2n_3-\beta n_1)+\frac{\gamma n_3(1-2n_2^2)+\alpha n_1n_2}{\theta}
$$

$$
\frac{\partial r_{23}}{\partial d_3}=\frac{\partial (\gamma n_2n_3-\alpha n_1)}{\partial d_3}=n_3(\alpha n_2n_3-\beta n_1)+\frac{\gamma n_2(1-2n_3^2)+\alpha n_1n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{31}}{\partial d_1}=\frac{\partial (\gamma n_1n_3-\alpha n_2)}{\partial d_1}=n_1(\alpha n_1n_3-\beta n_2)+\frac{\gamma n_3(1-2n_1^2)+\alpha n_1n_2}{\theta}
$$

$$
\frac{\partial r_{31}}{\partial d_2}=\frac{\partial (\gamma n_1n_3-\alpha n_2)}{\partial d_2}=n_2(\alpha n_1n_3-\beta n_2)-\frac{\alpha(1-n_2^2)+2\gamma n_1n_2n_3}{\theta}
$$

$$
\frac{\partial r_{31}}{\partial d_3}=\frac{\partial (\gamma n_1n_3-\alpha n_2)}{\partial d_3}=n_3(\alpha n_1n_3-\beta n_2)+\frac{\gamma n_1(1-2n_3^2)+\alpha n_2n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{32}}{\partial d_1}=\frac{\partial (\gamma n_2n_3+\alpha n_1)}{\partial d_1}=n_1(\alpha n_2n_3+\beta n_1)+\frac{\alpha(1-n_1^2)-2\gamma n_1n_2n_3}{\theta}
$$

$$
\frac{\partial r_{32}}{\partial d_2}=\frac{\partial (\gamma n_2n_3+\alpha n_1)}{\partial d_2}=n_2(\alpha n_2n_3+\beta n_1)+\frac{\gamma n_3(1-2n_2^2)-\alpha n_1n_2}{\theta}
$$

$$
\frac{\partial r_{32}}{\partial d_3}=\frac{\partial (\gamma n_2n_3+\alpha n_1)}{\partial d_3}=n_3(\alpha n_2n_3+\beta n_1)+\frac{\gamma n_2(1-2n_3^2)-\alpha n_1n_3}{\theta}
$$

$\rule{1000px}{0.4pt}$
$$
\frac{\partial r_{33}}{\partial d_1}=\frac{\partial (\beta+\gamma n_3^2)}{\partial d_1}=-\frac{2\gamma n_1n_3^2}{\theta}+\alpha n_1(n_3^2-1)
$$

$$
\frac{\partial r_{33}}{\partial d_2}=\frac{\partial (\beta+\gamma n_3^2)}{\partial d_2}=-\frac{2\gamma n_2n_3^2}{\theta}+\alpha n_2(n_3^2-1)
$$

$$
\frac{\partial r_{33}}{\partial d_3}=\frac{\partial (\beta+\gamma n_3^2)}{\partial d_3}=\frac{2\gamma n_3(1-n_3^2)}{\theta}+\alpha n_3(n_3^2-1)
$$

$\rule{1000px}{0.4pt}$

So the final answer is:
$$
\frac{d\bold r}{d\bold {d}^T}=\begin {bmatrix}\frac{2\gamma n_1(1-n_1^2)}{\theta}+\alpha n_1(n_1^2-1)&-\frac{2\gamma n_1^2n_2}{\theta}+\alpha n_2(n_1^2-1)&-\frac{2\gamma n_1^2n_3}{\theta}+\alpha n_3(n_1^2-1)\\n_1(\alpha n_1n_2-\beta n_3)+\frac{\gamma n_2(1-2n_1^2)+\alpha n_1n_3}{\theta}&n_2(\alpha n_1n_2-\beta n_3)+\frac{\gamma n_1(1-2n_2^2)+\alpha n_2n_3}{\theta}&n_3(\alpha n_1n_2-\beta n_3)+\frac{\alpha (n_3^2-1)-2\gamma n_1n_2n_3}{\theta}\\n_1(\alpha n_1n_3+\beta n_2)+\frac{\gamma n_3(1-2n_1^2)-\alpha n_1n_2}{\theta}&n_2(\alpha n_1n_3+\beta n_2)+\frac{\alpha(1-n_2^2)-2\gamma n_1n_2n_3}{\theta}&n_3(\alpha n_1n_3+\beta n_2)+\frac{\gamma n_1(1-2n_3^2)-\alpha n_2n_3}{\theta}\\n_1(\alpha n_1n_2+\beta n_3)+\frac{\gamma n_2(1-2n_1^2)-\alpha n_1n_3}{\theta}&n_2(\alpha n_1n_2+\beta n_3)+\frac{\gamma n_1(1-2n_2^2)-\alpha n_2n_3}{\theta}&n_3(\alpha n_1n_2+\beta n_3)+\frac{\alpha(1-n_3^2)-2\gamma n_1n_2n_3}{\theta}\\-\frac{2\gamma n_1n_2^2}{\theta}+\alpha n_1(n_2^2-1)&\frac{2\gamma n_2(1-n_2^2)}{\theta}+\alpha n_2(n_2^2-1)&-\frac{2\gamma n_2^2n_3}{\theta}+\alpha n_3(n_2^2-1)\\n_1(\alpha n_2n_3-\beta n_1)-\frac{\alpha(1-n_1^2)+2\gamma n_1n_2n_3}{\theta}&n_2(\alpha n_2n_3-\beta n_1)+\frac{\gamma n_3(1-2n_2^2)+\alpha n_1n_2}{\theta}&n_3(\alpha n_2n_3-\beta n_1)+\frac{\gamma n_2(1-2n_3^2)+\alpha n_1n_3}{\theta}\\n_1(\alpha n_1n_3-\beta n_2)+\frac{\gamma n_3(1-2n_1^2)+\alpha n_1n_2}{\theta}&n_2(\alpha n_1n_3-\beta n_2)-\frac{\alpha(1-n_2^2)+2\gamma n_1n_2n_3}{\theta}&n_3(\alpha n_1n_3-\beta n_2)+\frac{\gamma n_1(1-2n_3^2)+\alpha n_2n_3}{\theta}\\n_1(\alpha n_2n_3+\beta n_1)+\frac{\alpha(1-n_1^2)-2\gamma n_1n_2n_3}{\theta}&n_2(\alpha n_2n_3+\beta n_1)+\frac{\gamma n_3(1-2n_2^2)-\alpha n_1n_2}{\theta}&n_3(\alpha n_2n_3+\beta n_1)+\frac{\gamma n_2(1-2n_3^2)-\alpha n_1n_3}{\theta}\\-\frac{2\gamma n_1n_3^2}{\theta}+\alpha n_1(n_3^2-1)&-\frac{2\gamma n_2n_3^2}{\theta}+\alpha n_2(n_3^2-1)&\frac{2\gamma n_3(1-n_3^2)}{\theta}+\alpha n_3(n_3^2-1)\end {bmatrix}
$$
That is the same result as that found in the textbook.

