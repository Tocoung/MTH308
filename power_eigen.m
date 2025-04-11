A=[3,0,0;
    -4,6,2;
    16,-15,-5];
x=[1;
    0.5;
    0.25];
i=10;
format long;
for k=1:i
    y=A*x;
    mu=max(abs(y));
    x=y/mu;
    disp(y);
end
