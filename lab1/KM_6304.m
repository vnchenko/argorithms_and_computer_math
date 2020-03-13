A = [3 2 1; 1 12 2; 1 2 3; 4 2 1]
B = [3 2 1 3]
N = 4;

##A = [1 6 1; 3 7 12; 5 8 13; 7 9 14; 9 10 5]
##B = [5 5 5 5 5]
##N = 5;

[U, S, V] = svd(A);
S1 = diag(diag(1./S))*eye(3, N);
X = V*S1*U'*B'

#--------------------------------
if N == 4
  U;
  A_mul_AT = A*A';
  [eig_U, q] = eig(A_mul_AT);
  buf = eig_U(:,1);
  eig_U(:, 1) = eig_U(:, 4);
  eig_U(:, 4) = buf;
  buf = eig_U(:,2);
  eig_U(:, 2) = eig_U(:, 3);
  eig_U(:, 3) = buf;
  for i = [1 2]
      eig_U(:, i) = -1 * eig_U(:, i);
  endfor
  U_new = eig_U;


  S;
  [q, S_eig] = eig(A_mul_AT);
  S_eig = flip(diag(S_eig))(1:3);
  S_new = [];
  for i = 1:length(S_eig)
      S_new = [S_new real(sqrt(S_eig(i)))];
  endfor
  S_new;

  # print(V)
  AT_mul_A = A'*A;
  [eig_V, q] = eig(AT_mul_A);
  buf = eig_V(:,1);
  eig_V(:, 1) = eig_V(:, 3);
  eig_V(:, 3) = buf;
  eig_V = eig_V';
  for i = [1]
      eig_V(i, :) = -1*eig_V(i, :);
  endfor
  V_new = eig_V;
else
  U;
  A_mul_AT = A*A';
  [eig_U, q] = eig(A_mul_AT);
  buf = eig_U(:,1);
  eig_U(:, 1) = eig_U(:, 5);
  eig_U(:, 5) = buf;
  buf = eig_U(:,2);
  eig_U(:, 2) = eig_U(:, 4);
  eig_U(:, 4) = buf;
  for i = [1 2 3 5]
      eig_U(:, i) = -1 * eig_U(:, i);
  endfor
  U_new = eig_U;


  S;
  [q, S_eig] = eig(A_mul_AT);
  S_eig = flip(diag(S_eig))(1:3);
  S_new = [];
  for i = 1:length(S_eig)
      S_new = [S_new real(sqrt(S_eig(i)))];
  endfor
  S_new;

  V;
  AT_mul_A = A'*A;
  [eig_V, q] = eig(AT_mul_A);
  buf = eig_V(:,1);
  eig_V(:, 1) = eig_V(:, 3);
  eig_V(:, 3) = buf;
##  eig_V = eig_V';
  for i = [1]
      eig_V(:, i) = -1*eig_V(:, i);
  endfor
  V_new = eig_V;
endif
S1 = diag(diag(1./S))*eye(3, N);
X1 = V*S1*U'*B'
