

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *


class Detect_Ingles(BaseModel):
    flag: bool

async def DetectEnglish(
        text: str,
        model: str = "gpt-4.1-nano",
        logger= "",

    ):
    content_ = f"""
{text}
    """
    prompt_system = """
Detecte se o texto enviado pelo usuario esta em ingles
    """
    agent = Agent(name="Detect English", instructions=prompt_system, model=model, output_type=Detect_Ingles)
    result = await Runner.run(agent, content_, max_turns=300)
    final_output = result.final_output.flag
    logger.info(f"RAW OUTPUT: {result.final_output}")
    
    return final_output
