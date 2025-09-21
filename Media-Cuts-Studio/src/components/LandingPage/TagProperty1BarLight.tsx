import { IconsIconsArrowW } from "@/components/LandingPage/IconsIconsArrowW";

export interface ITagProperty1BarLightProps {
  text?: string;
  text2?: string;
  property1?: "bar-dark" | "bar-light";
  className?: string;
}

export const TagProperty1BarLight = ({
  text = "Version Beta 1.0",
  property1 = "bar-dark",
  className,
  ...props
}: ITagProperty1BarLightProps): JSX.Element => {
  const variantsClassName = "property-1-" + property1;

  return (
    <div
      className={
        "rounded-[10px] border-solid border-[rgba(34,34,34,0.10)] border pt-2.5 pr-[13px] pb-2.5 pl-[13px] flex items-center justify-center w-[229px] h-[31px] relative overflow-hidden " +
        className +
        " " +
        variantsClassName
      }
    >
      <div
        className="text-[rgba(255,255,255,0.50)] text-center font-tag-font-family text-tag-font-size leading-tag-line-height font-tag-font-weight relative"
        style={{ letterSpacing: "var(--tag-letter-spacing, -0.025em)" }}
      >
        {text}
      </div>
    </div>
  );
};
