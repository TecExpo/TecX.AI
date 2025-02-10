// Format date to readable string
export const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};

// Format number with commas
export const formatNumber = (number) => {
  return new Intl.NumberFormat().format(number);
};

// Convert text to capitalize case
export const capitalizeText = (text) => {
  return text.charAt(0).toUpperCase() + text.slice(1);
};
