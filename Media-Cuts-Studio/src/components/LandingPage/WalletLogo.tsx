export interface IWalletLogoProps {
  text?: string;
  className?: string;
}

export const WalletLogo = ({
  text = "undefined",
  className,
  ...props
}: IWalletLogoProps): JSX.Element => {
  return (
    <div className={"w-[89px] h-[34px] relative " + className}>
      <div className="bg-[rgba(255,255,255,0.00)] w-[100%] h-[100%] absolute right-[0%] left-[0%] bottom-[0%] top-[0%]"></div>
      <div className="text-white text-left font-['Poppins-SemiBold',_sans-serif] text-2xl leading-6 font-semibold absolute right-[29.21%] left-[5.62%] w-[65.17%] bottom-[14.71%] top-[14.71%] h-[70.59%] flex items-center justify-start">
        Logo{" "}
      </div>
    </div>
  );
};
