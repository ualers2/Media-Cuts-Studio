import hashlib
import time
import requests
import yt_dlp
import os
import unicodedata
import re
from termcolor import cprint
from pathlib import Path
from difflib import SequenceMatcher
from agents import Agent,  ItemHelpers, Runner,RunHooks, handoff, ModelSettings , RunConfig, RunContextWrapper, Usage
import requests
import asyncio
import subprocess
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import cv2
from firebase_admin import db
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from pydantic import BaseModel
from openai.types.responses import ResponseCompletedEvent, ResponseTextDeltaEvent
import yt_dlp
import time
import unicodedata
import json
import re
import textwrap
import hashlib
from pathlib import Path
from difflib import SequenceMatcher
from datetime import datetime, timedelta
import requests
import srt
import pytz
from typing import List
from termcolor import cprint
from dotenv import load_dotenv
import math