export const requiredRule = (field) => (v) => !!v || `${field} é obrigatório`;

export const lessThanRule = (max) => (v) => (v && v.length <= max) || `Tem que ter menos de ${max} caracteres`;

export const moreThanRule = (min) => (v) => (v && v.length >= min) || `Tem que ter mais de ${min} caracteres`;

export const mustHaveNumberRule = (num) => (v) => (v && v.length === num) || `Tem que ter ${num} caracteres`;

export const foneRule = (num) => (v) => {
  const fone = v.replace(/\(/g, '').replace(/\)/g, '').replace(/ /g, '').replace(/-/g, '');
  return (v && fone.length >= num) || `Tem que ter ${num} caracteres`;
};

export const emailRule = () => (v) => /.+@.+\..+/.test(v) || 'E-mail inválido';
export const mustBeEqualPass = (val) => (v) => val === v || 'Deve ser igual a senha';

export const cpflRule = () => (v) => {
  const erroMsg = 'CPF não valido';
  // eslint-disable-next-line no-useless-escape
  const strCPF = v.replace(/\./g, '').replace(/-/g, '');
  let Soma = 0;
  let Resto = 0;
  Soma = 0;
  if (strCPF === '00000000000') { return erroMsg; }

  // eslint-disable-next-line no-plusplus
  for (let i = 1; i <= 9; i++) {
    // eslint-disable-next-line radix
    Soma += parseInt(strCPF.substring(i - 1, i)) * (11 - i);
  }
  Resto = (Soma * 10) % 11;

  if ((Resto === 10) || (Resto === 11)) Resto = 0;
  // eslint-disable-next-line radix
  if (Resto !== parseInt(strCPF.substring(9, 10))) { return erroMsg; }

  Soma = 0;
  // eslint-disable-next-line no-plusplus
  for (let i = 1; i <= 10; i++) {
    // eslint-disable-next-line radix
    Soma += parseInt(strCPF.substring(i - 1, i)) * (12 - i);
  }
  Resto = (Soma * 10) % 11;

  if ((Resto === 10) || (Resto === 11)) Resto = 0;
  // eslint-disable-next-line radix
  if (Resto !== parseInt(strCPF.substring(10, 11))) { return erroMsg; }
  return true;
};

export default {
  requiredRule,
  lessThanRule,
  moreThanRule,
  mustHaveNumberRule,
  foneRule,
  emailRule,
  cpflRule,
  mustBeEqualPass,
};
