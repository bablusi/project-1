import streamlit as st
from config import *

from collections import deque
import argparse
import imutils.image import ImageStream
import time
import cv2
import numpy as np
import argparse
import sys


st.sidebar.header('PROJECT_NAME')
st.sidebar.radio("Project menu",MENU_OPTION)