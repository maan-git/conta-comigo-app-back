import moment from 'moment';

export const formatDate = (dateStr) => moment(String(dateStr)).format('DD/MM/YY');

export const calcAge = (dateString) => moment().diff(moment(dateString, 'YYYYMMDD'), 'years');


export const isRiskGroup = (value) => {
  if (value === false) {
    return 'Não';
  }
  return 'Sim';
};

export const calcTimeCard = (dateCard) => {
  const resText = 'há ';
  const dtMonthsCompare = moment().diff(moment(dateCard, 'YYYYMMDD'), 'months');
  if (dtMonthsCompare > 1) {
    return resText.concat(dtMonthsCompare).concat(' meses');
  }

  const dtDaysCompare = moment().diff(moment(dateCard, 'YYYYMMDD'), 'days');
  if (dtDaysCompare > 1) {
    return resText.concat(dtDaysCompare).concat(' dias');
  }

  const dtHoursCompare = moment().diff(moment(dateCard, 'YYYYMMDDHHmmss'), 'hours');
  if (dtHoursCompare > 1) {
    return resText.concat(dtHoursCompare).concat(' horas');
  }

  const dtMinutesCompare = moment().diff(moment(dateCard, 'YYYYMMDDHHmmss'), 'minutes');
  if (dtMinutesCompare > 1) {
    return resText.concat(dtMinutesCompare).concat(' minutos');
  }

  return resText.concat(' pouco tempo');
};

export default {
  formatDate,
  calcAge,
  calcTimeCard,
};
