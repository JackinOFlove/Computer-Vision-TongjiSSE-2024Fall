# Problem1

## 1. Problem Description

Please prove that $L(\bold h)$ is a strictly convex function. 
$$
L(\bold h)=\frac{1}{2}(f(\bold x+\bold h))^Tf(\bold x +\bold h)+\frac{1}{2}\mu \bold h^T \bold h\\
=\frac{1}{2}(f(\bold x))^Tf(\bold x)+\bold h^T(\bold J(\bold x))^Tf(\bold x)+\frac{1}{2}\bold h^T(\bold J(\bold x))^T\bold J(\bold x)\bold h+\frac{1}{2}\mu\bold h^T \bold h
$$
where $\bold J(\bold x)$ is $f(\bold x)$'s Jacobian matrix, and $\mu >0$ is the damped coefficient. 

## 2. Problem Solution

According to the prompts given by the title, If a function $L(\bold h)$ is differentiable up to at least second order, $L$ is strictly convex if its Hessian matrix is positive definite.)
$$
L(\bold h)
=\frac{1}{2}(f(\bold x))^Tf(\bold x)+\bold h^T(\bold J(\bold x))^Tf(\bold x)+\frac{1}{2}\bold h^T(\bold J(\bold x))^T\bold J(\bold x)\bold h+\frac{1}{2}\mu\bold h^T \bold h
$$
so we can calculate derivative of $L(\bold h)$ to the first order (Jacobian matrix):
$$
∇L(\bold h)=(\bold J(\bold x))^Tf(\bold x)+(\bold J(\bold x))^T\bold J(\bold x)\bold h+\mu \bold h
$$
And then, we can calculate derivative of $L(\bold h)$ to the second order (Hessian matrix):
$$
∇^2L(\bold h)=(\bold J(\bold x))^T\bold J(\bold x)\bold +\mu \bold I = \bold H(\bold h)
$$
$∇L(\bold h)\in R^n$ and $∇^2L(\bold h)\in R^{n \times n}$. $I$ is the indentity matrix. Next, we should prove that $\bold H(\bold h)$ is positive definite.

For all $\bold x \in R^n$ and $\bold x \neq 0$, we have:
$$
\bold x^T\bold H(\bold h)\bold x=\bold x^T(\bold J(\bold x))^T\bold J(\bold x)\bold x+\bold x^T\mu I\bold x\\=(\bold J(\bold x)\bold x)^T\bold J(\bold x)\bold x+\mu \bold x^T\bold x\\=||\bold J(\bold x)\bold x||^2_2+\mu ||\bold x||^2_2
$$
Obviously, $||\bold J(\bold x)\bold x||^2_2\geq 0$. Beacause $\mu >0$ is the damped coefficient, so $\mu ||\bold x||^2_2 >0$. Therefore, $\bold x^T\bold H(\bold h)\bold x>0$. So $\bold H(\bold x)$ is positive definite, and $L(\bold h)$ is a strictly convex function. 