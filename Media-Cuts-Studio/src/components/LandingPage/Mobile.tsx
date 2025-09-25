import { TagProperty1BarLight } from "@/components/LandingPage/TagProperty1BarLight";
import { CtaProperty1DarkProperty2M } from "@/components/LandingPage/CtaProperty1DarkProperty2M";
import { IconsIconsTick } from "@/components/LandingPage/IconsIconsTick";
import { CtaProperty1PurpleProperty2M } from "@/components/LandingPage/CtaProperty1PurpleProperty2M";
import { WalletLogo } from "@/components/LandingPage/WalletLogo";

export interface IMobileProps {
  className?: string;
}

export const Mobile = ({ className, ...props }: IMobileProps): JSX.Element => {
  return (
    
    <div
      className={
        "bg-[#ffffff] relative overflow-hidden" + className
      }
    >
      <div
        className="max-w-md mx-auto px-4 sm:px-6 lg:px-8"
        style={{
          background:
            "linear-gradient(180deg, rgba(0, 0, 0, 1.00) 0%,rgba(70, 33, 126, 1.00) 34.359997510910034%,rgba(5, 2, 10, 1.00) 100%)",
        }}
      ></div>
      <div className="flex flex-col items-start justify-start h-[5169px] absolute left-0 top-0">
        <div className="relative overflow-hidden w-full max-w-md mx-auto px-4 py-8">
          {/* background escuro ocupa todo o container */}
           <div className="absolute inset-0 bg-black"></div>

           {/* Conteúdo centralizado */}
           <div className="relative flex flex-col items-center justify-center gap-4 py-12">
             <h2
               className="text-3xl sm:text-4xl md:text-5xl text-center font-bold 
                          bg-gradient-to-b from-white via-white via-indigo-700 to-white 
                          bg-clip-text text-transparent"
             >
               Turn long videos into
               <br />
               short messages
             </h2>
             <img
               className="w-12 h-14"
               style={{ objectFit: "cover" }}
               src="message-10.png"
               alt="ícone de mensagem"
             />
           </div>
+
           {/* Ícone de cursor flutuante */}
           <img
             className="absolute top-4 left-4 w-14 h-12 transform rotate-90"
             style={{ objectFit: "cover" }}
             src="cursor-20.png"
             alt="cursor rotacionado"
           />
        </div>
        <div
          className="bg-[#000000] shrink-0 w-[389px] h-[4836px] relative overflow-hidden"
          style={{ margin: "-6px 0 0 0" }}
        >
          <div
            className="pt-[5px] flex flex-col gap-0 items-center justify-start w-[390px] h-[306px] absolute left-[50%] top-[-17px]"
            style={{ translate: "-50%" }}
          >
            <div className="flex flex-col gap-5 items-center justify-start shrink-0 w-[390px] h-[135px] relative">
              <div className="flex flex-col gap-1.5 items-center justify-start self-stretch shrink-0 h-[140px] relative">
                <div
                  className="text-[#ffffff] text-center font-h4-font-family text-h4-font-size leading-h4-line-height font-h4-font-weight relative self-stretch h-12"
                  style={{
                    letterSpacing: "var(--h4-letter-spacing, -0.04em)",
                    webkitTextStroke: "1px #081f0c",
                  }}
                >
                  Media Cuts Studio{" "}
                </div>
                <div
                  className="text-[#ffffff] text-center font-tag-font-family text-tag-font-size leading-tag-line-height font-tag-font-weight relative w-[357px]"
                  style={{
                    letterSpacing: "var(--tag-letter-spacing, -0.025em)",
                  }}
                >
                  Post every day without editing anything.{" "}
                </div>
                <TagProperty1BarLight
                  text="Version Beta 1.0"
                  property1="bar-light"
                  className="!border-[#222222] !shrink-0"
                ></TagProperty1BarLight>
              </div>
            </div>
            <div className="flex flex-row gap-6 items-center justify-start shrink-0 relative">
              <div className="bg-[#100720] rounded-[30px] pt-3 pr-6 pb-3 pl-6 flex flex-row gap-2.5 items-start justify-start shrink-0 relative">
                <button
                  onClick={() => (window.location.href = "/login")}
                  className="text-primary-0 text-justified font-semibold-type16-font-family text-semibold-type16-font-size leading-semibold-type16-line-height font-semibold-type16-font-weight relative"
                  style={{
                    letterSpacing: "var(--semibold-type16-letter-spacing, -0.02em)",
                    background: "none",
                    border: "none",
                    padding: 0,
                    margin: 0,
                    cursor: "pointer",
                  }}
                >
                  Get the free plan
                </button>
              </div>
              <div className="rounded-[30px] border-solid border-[rgba(0,0,0,0.16)] border pt-3 pr-6 pb-3 pl-6 flex flex-row gap-2.5 items-start justify-start shrink-0 relative">
                <a
                  href="#our-pricing"
                  className="text-[#7eabe6] text-justified font-medium-type18-font-family text-medium-type18-font-size leading-medium-type18-line-height font-medium-type18-font-weight relative"
                  style={{
                    letterSpacing: "var(--medium-type18-letter-spacing, -0.02em)",
                    cursor: "pointer",
                  }}
                >
                  See Pricing
                </a>
              </div>
            </div>
          </div>
          <div className="w-[390px] h-[1947px] absolute left-0 top-[1465px] overflow-hidden">
            <div className="w-[305px] h-[596px] absolute left-[42px] top-[1307px]">
              <div className="bg-[rgba(0,0,0,0.06)] rounded-[10px] border-solid border-[rgba(255,255,255,0.15)] border w-[100%] h-[100%] absolute right-[-0.16%] left-[0.16%] bottom-[0.05%] top-[-0.05%]"></div>
              <CtaProperty1DarkProperty2M
                text="Whitelist to Become a Studio"
                property1="dark"
                property2="m"
                className="!w-[86.97%] !absolute !right-[6.47%] !left-[6.56%] !top-[calc(50%_-_-231.5px)]"
              ></CtaProperty1DarkProperty2M>
              <div
                className="border-solid border-[#282729] border-t border-r-[0] border-b-[0] border-l-[0] w-[100%] h-[0%] absolute right-[0%] left-[0%] bottom-[85.82%] top-[14.18%]"
                style={{
                  marginTop: "-1px",
                  transformOrigin: "0 0",
                  transform: "rotate(-0.194deg) scale(1, 1)",
                }}
              ></div>
              <div className="flex flex-col gap-0 items-start justify-start w-[284px] h-[498px] absolute left-3 top-[19.5px]">
                <div className="flex flex-col gap-1.5 items-start justify-start shrink-0 w-[268px] relative">
                  <div
                    className="text-[#ffffff] text-left font-['Inter-Medium',_sans-serif] text-2xl leading-[31px] font-medium relative self-stretch flex items-center justify-start"
                    style={{ letterSpacing: "-0.0004em" }}
                  >
                    Studio{" "}
                  </div>
                  <div
                    className="text-[rgba(255,255,255,0.70)] text-left font-body-m-font-family text-body-m-font-size leading-body-m-line-height font-body-m-font-weight relative self-stretch h-8 flex items-center justify-start"
                    style={{
                      letterSpacing: "var(--body-m-letter-spacing, -0.0001em)",
                    }}
                  >
                    $54,18/mo{" "}
                  </div>
                </div>
                <div className="flex flex-col gap-0 items-start justify-start shrink-0 w-[282px] h-[417px] relative">
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[282px] h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[262px] h-4 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Dedicated Server 4 vCPU 16GB of RAM{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[270px] h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[244px] h-4 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Native Control Panel for Windows{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[250px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Shortify Algorithm for ∞ channels{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[264px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Batch algorithm for 50 videos per day{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[39px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[252px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      1 Weekly Reporting Agent{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[23px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Upload 1 The base Video{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[270px] h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[252px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Upload Cuts For Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Add ∞ Account Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[264px] h-[34px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Control ∞ Themes{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[251px] h-3 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      200 Requests per day{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[35px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[143px] h-3 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      24/7 Support{" "}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="w-[306px] h-[596px] absolute left-[46px] top-[660px]">
              <div
                className="rounded-[10px] w-[100%] h-[99.21%] absolute right-[0%] left-[0%] bottom-[0.79%] top-[0%]"
                style={{
                  background:
                    "linear-gradient(180deg, rgba(1, 0, 2, 1.00) 0%,rgba(54, 23, 100, 1.00) 100%)",
                  boxShadow: "0px 10px 74px 10px rgba(78, 0, 191, 0.41)",
                }}
              ></div>
              <div
                className="border-solid border-[#282729] border-t border-r-[0] border-b-[0] border-l-[0] w-[100%] h-[0%] absolute right-[0%] left-[0%] bottom-[84.98%] top-[15.02%]"
                style={{
                  marginTop: "-1px",
                  transformOrigin: "0 0",
                  transform: "rotate(0.002deg) scale(1, 1)",
                }}
              ></div>
              <img
                className="w-[100%] h-[100%] absolute right-[0%] left-[0%] bottom-[0%] top-[0%] overflow-visible"
                style={{ opacity: "0.3" }}
                src="pattern0.svg"
              />
              <CtaProperty1PurpleProperty2M
                text="Start creating content"
                property2="m"
                className="!w-[86.97%] !absolute !right-[6.49%] !left-[6.54%] !top-[calc(50%_-_-229.5px)]"
              ></CtaProperty1PurpleProperty2M>
              <div className="flex flex-col gap-2.5 items-start justify-start w-[277px] h-[487px] absolute left-[19px] top-[19.5px]">
                <div className="flex flex-col gap-1.5 items-start justify-start shrink-0 w-[275px] h-[63px] relative">
                  <div
                    className="text-[#ffffff] text-left font-['Inter-Medium',_sans-serif] text-2xl leading-[31px] font-medium relative self-stretch flex items-center justify-start"
                    style={{ letterSpacing: "-0.0004em" }}
                  >
                    Content Creator{" "}
                  </div>
                  <div
                    className="text-[rgba(255,255,255,0.70)] text-left font-body-m-font-family text-body-m-font-size leading-body-m-line-height font-body-m-font-weight relative self-stretch h-[26px] flex items-center justify-start"
                    style={{
                      letterSpacing: "var(--body-m-letter-spacing, -0.0001em)",
                    }}
                  >
                    $8,89/mo{" "}
                  </div>
                </div>
                <div className="flex flex-col gap-0 items-start justify-start shrink-0 w-[278px] h-[398px] relative">
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-11 relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[258px] h-11 flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Shared Server{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-7 relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Native Control Panel for Windows{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[277px] h-[27px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[248px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Shortify Algorithm for 3 channels{" "}
                    </div>
                  </div>
                  <div className="pt-[5px] pb-[5px] flex flex-row gap-0.5 items-center justify-start shrink-0 w-[268px] h-[26px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[260px] h-4 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Batch Algorithm for 5 videos{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[26px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[238px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      1 Weekly Reporting Agent{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[26px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Upload 1 The base Video{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[23px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Upload Cuts For Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[26px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Add 3 Account Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[25px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Control 3 Themes{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[27px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[246px] h-3.5 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      50 Requests per day{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[268px] h-[27px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[246px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      24/7 Support{" "}
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="w-[307px] h-[596px] absolute left-[45px] top-3">
              <div className="bg-[rgba(99,0,185,0.06)] rounded-[10px] border-solid border-[rgba(255,255,255,0.15)] border w-[100%] h-[100%] absolute right-[0.16%] left-[-0.16%] bottom-[0.05%] top-[-0.05%]"></div>
              <CtaProperty1DarkProperty2M
                text="Join New Startup"
                property1="dark"
                property2="m"
                className="!w-[86.97%] !absolute !right-[6.51%] !left-[6.51%] !top-[calc(50%_-_-232.51px)]"
              ></CtaProperty1DarkProperty2M>
              <div
                className="border-solid border-[#282729] border-t border-r-[0] border-b-[0] border-l-[0] w-[100%] h-[0%] absolute right-[0%] left-[0%] bottom-[84.98%] top-[15.02%]"
                style={{
                  marginTop: "-1px",
                  transformOrigin: "0 0",
                  transform: "rotate(0deg) scale(1, 1)",
                }}
              ></div>
              <div className="flex flex-col gap-[7px] items-start justify-start w-[292px] h-[504px] absolute left-[7px] top-[26.5px]">
                <div className="flex flex-col gap-1.5 items-start justify-start shrink-0 relative">
                  <div
                    className="text-[#ffffff] text-left font-['Inter-Medium',_sans-serif] text-2xl leading-[31px] font-medium relative w-[147px] flex items-center justify-start"
                    style={{ letterSpacing: "-0.0004em" }}
                  >
                    Startup{" "}
                  </div>
                  <div
                    className="text-[rgba(255,255,255,0.70)] text-left font-body-m-font-family text-body-m-font-size leading-body-m-line-height font-body-m-font-weight relative w-[147px] flex items-center justify-start"
                    style={{
                      letterSpacing: "var(--body-m-letter-spacing, -0.0001em)",
                    }}
                  >
                    $0,00/mo{" "}
                  </div>
                </div>
                <div className="flex flex-col gap-0 items-start justify-start shrink-0 w-[285px] h-[434px] relative overflow-hidden">
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[267px] h-[33px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Shortify Algorithm for 1 channels{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start self-stretch shrink-0 h-[26px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[143px] h-6 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Control 1 Themes{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[284px] h-[33px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Add 1 Account Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[267px] h-[33px] relative">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-['Inter-Regular',_sans-serif] text-[15px] leading-[29px] font-normal relative w-[241px] h-[15px] flex items-center justify-start"
                      style={{ letterSpacing: "-0.0001em" }}
                    >
                      Upload Cuts For Tiktok{" "}
                    </div>
                  </div>
                  <div className="pt-2.5 pb-2.5 flex flex-row gap-[5px] items-center justify-start shrink-0 w-[277px] h-[26px] absolute left-[-0.5px] top-[126px]">
                    <IconsIconsTick
                      icons="tick"
                      className="!shrink-0 !w-[15px] !h-[15px]"
                    ></IconsIconsTick>
                    <div
                      className="text-[#ffffff] text-left font-body-s-font-family text-body-s-font-size leading-body-s-line-height font-body-s-font-weight relative w-[143px] h-6 flex items-center justify-start"
                      style={{
                        letterSpacing:
                          "var(--body-s-letter-spacing, -0.0001em)",
                      }}
                    >
                      Shared Server{" "}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div className="bg-[#ffffff] rounded-[20px] border-solid border-[#eaeaea] border w-96 h-[376px] absolute left-[3px] top-[3524px]"></div>
          <div
            className="text-[#343434] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-lg leading-7 font-semibold absolute left-[127px] top-[3564px]"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Briana Patton{" "}
          </div>
          <div
            className="text-[#969696] text-left font-['BeVietnamPro-Regular',_sans-serif] text-sm leading-[22px] font-normal absolute left-[127px] top-[3598px]"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Manager{" "}
          </div>
          <div
            className="text-[#969696] text-left font-['BeVietnamPro-Regular',_sans-serif] text-sm leading-6 font-normal absolute left-[35px] top-[3652px] w-80"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Sed mattis est eget penatibus mauris, sed condimentum vitae viverra.
            Ipsum ut aliquet et morbi ac in. Lacinia mattis eget nisl
            pellentesque non, porttitor. Vitae et vestibulum ac id. Dui aliquet
            porttitor libero consequat volutpat eget sed turpis. Feugiat
            maecenas commodo et morbi morbi gravida.{" "}
          </div>
          <img
            className="rounded-[50%] w-[72px] h-[72px] absolute left-[35px] top-[3556px]"
            style={{ objectFit: "cover" }}
            src="mask0.png"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[35px] top-[3844px] overflow-visible"
            src="star0.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[61px] top-[3844px] overflow-visible"
            src="star1.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[87px] top-[3844px] overflow-visible"
            src="star2.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[113px] top-[3844px] overflow-visible"
            src="star3.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[139px] top-[3844px] overflow-visible"
            src="star4.svg"
          />
          <div className="flex flex-col gap-0 items-end justify-start w-[31px] h-[231px] absolute left-[331px] top-[2834px]"></div>
          <div
            className="flex flex-col gap-0 items-end justify-start w-[29px] h-[220px] absolute left-[326px] top-[4953px]"
            style={{
              transformOrigin: "0 0",
              transform: "rotate(0deg) scale(1, 1)",
            }}
          >
            <div
              className="rounded-[20px] flex flex-col gap-0 items-start justify-start shrink-0 w-[325px] h-[157px] relative"
              style={{
                boxShadow:
                  "0px 0px 0px 1.17px rgba(255, 255, 255, 0.10),  0px 0px 0px 2.33px rgba(0, 0, 0, 0.05),  0px -2px 40px 0px rgba(187, 155, 255, 0.15),  0px -2px 10px 0px rgba(233, 223, 255, 0.30), inset 0px 0.58px 0px 0px rgba(255, 255, 255, 0.50), inset 0px 0.5px 0px 0px rgba(255, 255, 255, 0.50)",
              }}
            ></div>
          </div>
          <div className="flex flex-col gap-0 items-end justify-start w-10 h-[253px] absolute left-[341px] top-[4414px]"></div>
          <div className="flex flex-col gap-0 items-end justify-start w-[25px] h-[241px] absolute left-[335px] top-[3342px]"></div>
          <div className="flex flex-col gap-0 items-end justify-start w-[25px] h-[241px] absolute left-[337px] top-[3867px]">
            <div
              className="rounded-[20px] flex flex-col gap-0 items-start justify-start shrink-0 w-80 h-[197px] relative"
              style={{
                boxShadow:
                  "0px 0px 0px 1.17px rgba(255, 255, 255, 0.10),  0px 0px 0px 2.33px rgba(0, 0, 0, 0.05),  0px -2px 40px 0px rgba(187, 155, 255, 0.15),  0px -2px 10px 0px rgba(233, 223, 255, 0.30), inset 0px 0.58px 0px 0px rgba(255, 255, 255, 0.50), inset 0px 0.5px 0px 0px rgba(255, 255, 255, 0.50)",
              }}
            ></div>
          </div>
          <div
            className="text-[#ffffff] text-center font-['BeVietnamPro-Bold',_sans-serif] text-xl font-bold absolute left-[-1px] top-[189px] w-[390px] h-14"
            style={{ letterSpacing: "0.005em" }}
          >
            Automate your presence, <br />
            Scale your content.{" "}
          </div>
          <div className="bg-[#ffffff] rounded-[15px] border-solid border-[#eaeaea] border w-[276px] h-[344px] absolute left-14 top-[271px]"></div>
          <div className="bg-[#f2f2ff] rounded-[15px] w-16 h-16 absolute left-[88px] top-[303px]"></div>
          <div className="rounded-[15px] w-10 h-10 absolute left-[100px] top-[315px] overflow-hidden">
            <img
              className="h-[auto] absolute left-[3.33px] top-[6.67px] overflow-visible"
              src="group-240.svg"
            />
          </div>
          <div
            className="text-lg sm:text-xl text-gray-300 max-w-lg mx-auto font-body-medium-font-family text-body-medium-font-size leading-body-medium-line-height font-body-medium-font-weight absolute left-[88px] top-[437px] w-[212px]"
            style={{
              letterSpacing: "var(--body-medium-letter-spacing, -0.01em)",
            }}
          >
            Creation of automatic cuts
            <br />
            on specific days and times for a YouTube channel{" "}
          </div>
          <div
            className="text-[#6a4bff] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-base font-semibold absolute left-[88px] top-[560px]"
            style={{ letterSpacing: "-0.41px", textDecoration: "underline" }}
          >
            Learn more{" "}
          </div>
          <div
            className="text-[#343434] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-[22px] leading-[30px] font-semibold absolute left-[88px] top-[391px]"
            style={{ letterSpacing: "-0.41px" }}
          >
            Shortify{" "}
          </div>
          <div className="w-[276px] h-[344px] static">
            <div className="bg-[#ffffff] rounded-[15px] border-solid border-[#eaeaea] border w-[276px] h-[344px] absolute left-[49px] top-[651px]"></div>
            <div className="bg-[#f2f2ff] rounded-[15px] w-16 h-16 absolute left-[81px] top-[683px]"></div>
            <div className="rounded-[15px] w-10 h-10 absolute left-[93px] top-[695px] overflow-hidden">
              <img
                className="h-[auto] absolute left-[5px] top-[3.33px] overflow-visible"
                src="group-310.svg"
              />
            </div>
            <div
              className="text-[#000000] text-left font-body-medium-font-family text-body-medium-font-size leading-body-medium-line-height font-body-medium-font-weight absolute left-[81px] top-[817px] w-[212px]"
              style={{
                letterSpacing: "var(--body-medium-letter-spacing, -0.01em)",
              }}
            >
              You can add tiktok accounts to upload your cuts created by
              shortify algorithm{" "}
            </div>
            <div
              className="text-[#6a4bff] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-base font-semibold absolute left-[81px] top-[937px]"
              style={{ letterSpacing: "-0.41px", textDecoration: "underline" }}
            >
              Learn more{" "}
            </div>
            <div
              className="text-[#343434] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-[22px] leading-[30px] font-semibold absolute left-[81px] top-[771px]"
              style={{ letterSpacing: "-0.41px" }}
            >
              Tiktok Accounts{" "}
            </div>
          </div>
          <div className="bg-[#ffffff] rounded-[15px] border-solid border-[#eaeaea] border w-[276px] h-[344px] absolute left-[53px] top-[1021px]"></div>
          <div className="bg-[#f2f2ff] rounded-[15px] w-16 h-16 absolute left-[85px] top-[1053px]"></div>
          <div className="rounded-[15px] w-10 h-10 absolute left-[97px] top-[1065px] overflow-hidden">
            <img
              className="h-[auto] absolute left-[3.33px] top-[6.67px] overflow-visible"
              src="group-241.svg"
            />
          </div>
          <div
            className="text-[#343434] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-[22px] leading-[30px] font-semibold absolute left-[85px] top-[1141px]"
            style={{ letterSpacing: "-0.41px" }}
          >
            Upload Cuts{" "}
          </div>
          <div
            className="text-[#050505] text-left font-body-medium-font-family text-body-medium-font-size leading-body-medium-line-height font-body-medium-font-weight absolute left-[85px] top-[1187px] w-[212px]"
            style={{
              letterSpacing: "var(--body-medium-letter-spacing, -0.01em)",
            }}
          >
            You can upload your created cuts via shortify algorithm to your
            added account{" "}
          </div>
          <div
            className="text-[#6a4bff] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-base font-semibold absolute left-[85px] top-[1307px]"
            style={{ letterSpacing: "-0.41px", textDecoration: "underline" }}
          >
            Learn more{" "}
          </div>
          <div className="bg-[#ffffff] rounded-[20px] border-solid border-[#eaeaea] border w-96 h-[376px] absolute left-[3px] top-[3920px]"></div>
          <div
            className="text-[#343434] text-left font-['BeVietnamPro-SemiBold',_sans-serif] text-lg leading-7 font-semibold absolute left-[127px] top-[3960px]"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Imelda Cowen{" "}
          </div>
          <div
            className="text-[#969696] text-left font-['BeVietnamPro-Regular',_sans-serif] text-sm leading-[22px] font-normal absolute left-[127px] top-[3994px]"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Consultant{" "}
          </div>
          <div
            className="text-[#969696] text-left font-['BeVietnamPro-Regular',_sans-serif] text-sm leading-6 font-normal absolute left-[35px] top-[4048px] w-80"
            style={{ letterSpacing: "-0.0025em" }}
          >
            Sapien praesent tristique iaculis amet sit odio pellentesque. Sit
            nulla pretium amet, fames aenean. Nascetur augue vulputate sed
            pretium pretium. Scelerisque amet facilisis ut pulvinar morbi a
            egestas. Vel vulputate dolor nisl in non. Amet enim ultricies
            imperdiet ac.{" "}
          </div>
          <img
            className="rounded-[50%] w-[72px] h-[72px] absolute left-[35px] top-[3952px]"
            style={{ objectFit: "cover" }}
            src="mask1.png"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[35px] top-[4240px] overflow-visible"
            src="star5.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[61px] top-[4240px] overflow-visible"
            src="star6.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[87px] top-[4240px] overflow-visible"
            src="star7.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[113px] top-[4240px] overflow-visible"
            src="star8.svg"
          />
          <img
            className="rounded-[20px] w-6 h-6 absolute left-[139px] top-[4240px] overflow-visible"
            src="star9.svg"
          />
        </div>
      </div>
      <div
        id="our-pricing"
        className="text-[#ffffff] text-center font-['BeVietnamPro-Bold',_sans-serif] text-[40px] font-bold absolute left-0 top-[1735px] w-[389px] h-[57px]"
        style={{ letterSpacing: "0.005em" }}
      >
        Our pricing
      </div>
    </div>
  );
};
