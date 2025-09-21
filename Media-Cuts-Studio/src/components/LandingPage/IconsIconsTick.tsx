export interface IIconsIconsTickProps {
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

export const IconsIconsTick = ({
  icons = "ecosystem",
  className,
  ...props
}: IIconsIconsTickProps): JSX.Element => {
  const variantsClassName = "icons-" + icons;

  return (
    <img
      className={
        "shrink-0 w-[15px] h-[15px] relative overflow-visible " +
        className +
        " " +
        variantsClassName
      }
      src="icons-icons-tick.svg"
    />
  );
};
