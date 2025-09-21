

import os
PRODUCTION_ENV = os.getenv("PRODUCTION_ENV", "True")

if PRODUCTION_ENV == "True":
    # Production
    from Studio.Modules.__init_libs__ import *

elif PRODUCTION_ENV == "False":
    # Local test
    from Modules.__init_libs__ import *


class Translate(BaseModel):
    titulo_em_portugues: str

async def TranslateEnglishtoPortuguese(
        text: str,
        model: str = "gpt-4.1-nano",
        logger= ""
    ):
    content_ = f"""
{text}
    """
    prompt_system = """
traduza todo os textos recebidos para portugues brasil
    """
    agent = Agent(name="Translate English to Portuguese", instructions=prompt_system, model=model, output_type=Translate)
    result = await Runner.run(agent, content_, max_turns=300)
    final_output = result.final_output.titulo_em_portugues
    logger.info(f"RAW OUTPUT: {result.final_output}")
    return final_output
