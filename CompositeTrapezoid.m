f = @(x) x.^3;
a = 1;
b = 2;
n = 4;
h = (b - a) / n;
sum = f(a) + f(b);
for i = 1:n-1
    x = a + i * h;
    sum = sum + 2 * f(x);
end
integral_approx = (h / 2) * sum;
fprintf('Approximate integral of x^3 from %.1f to %.1f is %.10f\n', a, b, integral_approx);
