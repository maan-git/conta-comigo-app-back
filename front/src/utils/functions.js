/**
 * Generates a GUID string.
 * @returns {string} The generated GUID.
 * @example af8a8416-6e18-a307-bd9c-f2c947bbb3aa
 * @author Slavik Meltser.
 * @link http://slavik.meltser.info/?p=142
 */

const p8 = (s) => {
  const p = (`${Math.random().toString(16)} 000000000`).substr(2, 8);
  return s ? `-${p.substr(0, 4)}-${p.substr(4, 4)}` : p;
};

export const guid = () => p8() + p8(true) + p8(true) + p8();

export default {
  guid,
};
