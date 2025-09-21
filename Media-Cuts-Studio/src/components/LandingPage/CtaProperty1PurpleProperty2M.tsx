export interface ICtaProperty1PurpleProperty2MProps {
  text?: string;
  property1?: "dark" | "purple" | "white";
  property2?: "m" | "s";
  className?: string;
}

export const CtaProperty1PurpleProperty2M = ({
  text = "Join waitlist",
  property1 = "purple",
  property2 = "s",
  className,
  ...props
}: ICtaProperty1PurpleProperty2MProps): JSX.Element => {
  const variantsClassName =
    "property-1-" + property1 + " property-2-" + property2;

  return (
    <div
      className={
        "bg-[rgba(140,69,255,0.40)] rounded-[10px] border-solid border-[rgba(255,255,255,0.15)] border pt-1.5 pr-[15px] pb-1.5 pl-[15px] flex flex-row gap-2.5 items-center justify-center w-[267px] relative overflow-hidden " +
        className +
        " " +
        variantsClassName
      }
      style={{
        boxShadow: "inset 0px 0px 6px 3px rgba(255, 255, 255, 0.25)",
        backdropFilter: "blur(7px)",
      }}
    >
      <div
        className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative flex items-center justify-start"
        style={{ letterSpacing: "var(--body-s-letter-spacing, -0.0001em)" }}
      >
        {text}{" "}
      </div>
    </div>
  );
};
