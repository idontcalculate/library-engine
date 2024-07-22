const Input = ({ type, value, onChange, placeholder, className }) => (
    <input
      type={type}
      value={value}
      onChange={onChange}
      placeholder={placeholder}
      className={className}
    />
  );
  
  export default Input;
  