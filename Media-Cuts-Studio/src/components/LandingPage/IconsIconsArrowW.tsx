export interface IIconsIconsArrowWProps {
  icons?:
    | "ecosystem"
    | "target"
    | "lock"
    | "notifications"
    | "arrow-w"
    | "arrow-b"
    | "tick"
    | "target-white"
    | "lock-white"
    | "notifications-white"
    | "tick-white"
    | "ecosystem-white"
    | "menu"
    | "menu-w";
  className?: string;
}

export const IconsIconsArrowW = ({
  icons = "ecosystem",
  className,
  ...props
}: IIconsIconsArrowWProps): JSX.Element => {
  const variantsClassName = "icons-" + icons;

  return (
    <img
      className={
        "shrink-0 w-4 h-4 relative overflow-visible " +
        className +
        " " +
        variantsClassName
      }
      src="icons-icons-arrow-w.svg"
    />
  );
};
