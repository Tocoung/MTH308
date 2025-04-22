f = @(x, y) (x - y)/2;
x0 = 0;
y0 = 1;
h = 0.1;
n = 2;
x = x0;
y = y0;
for i = 1:n
    k1 = h * f(x, y);
    k2 = h * f(x + h/2, y + k1/2);
    k3 = h * f(x + h/2, y + k2/2);
    k4 = h * f(x + h, y + k3);
    y = y + (1/6)*(k1 + 2*k2 + 2*k3 + k4);
    x = x + h;
    fprintf('After step %d: x = %.1f, y = %.10f\n', i, x, y);
end
fprintf('\nApproximate value of y(0.2) = %.10f\n', y);
