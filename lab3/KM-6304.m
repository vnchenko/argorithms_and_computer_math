h = 0.1
a = 1
b = 2
y0 = -1
z0 = 0

function output = myode45(t, y)
  output = [y(2); 2*y(2) + exp(t)];
endfunction


function[y,t]=eiler(a,b,h,y0,z0)
  n = (b-a)/h;
  y(1,:) = [y0, z0];
  
  for i = 1:n+1 
    t(i) = a + (i-1)*h;
  end

  for i = 2:n+1
    temporary = myode45(t(i-1),y(i-1,:));
    y(i,:) = [y(i-1, 1)+h*temporary(1) y(i-1,2)+h*temporary(2)];
  end
end



par=odeset ('InitialStep' ,h , 'MaxStep' ,h) ; 
[t_1, y_1] = ode45("@myode45", [a, b], [y0, z0], par)
[y_2,t_2] = eiler(a, b, h, y0, z0)
plot(t_1, y_1(:,1), "-o", t_2, y_2(:,1), "-o"), title('y');
figure;
plot(t_1, y_1(:,2), "-o", t_2, y_2(:,2), "-o"), title('y_dot');


