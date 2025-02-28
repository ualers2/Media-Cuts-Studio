# Media Cuts Studio

# Release Build 0.0.1
#### Section - Login
- ✅ Login area integrated into the panel
- ✅ Authentication via Landing page API endpoint
- ✅ Creation and loading of user session Keeping login for 5h
- ✅ Error Modal CustomModals for "The user field is empty."
- ✅ Error Modal CustomModals for "The password field is empty."
- ✅ Receives expire_time_license and api_key from login endpoint
- ✅ Custom Modal settings to display valid login session time
- ✅ self.session_flag for session control when trying to navigate to other dashboard sections without login
- ✅ Modal Warning CustomModals for "You must be logged in to access this section" which is displayed when self.session_flag is False
#### Section - Control Panel
- ✅ Display of welcome message with email without "@gmail.com" 
- ✅ Display of the last login made by the user 
- ✅ Button to go to account with email without the user's "@gmail.com" 
- ✅ Menu opens when login is done
- ✅ Mode Shortify when clicked takes you to the Mode Shortify subsection (it is the default subsection when logging in)
- ✅ Mode Batch processing when clicked takes you to the Batch Processing Mode subsection
- ✅ Mode 1 long video when clicked takes you to the Mode 1 long video subsection
###### Mode Shortify
- ✅ Start Shortify button to start the Algorithm 
- ✅ Yt channel: To receive the name of the channel to be scheduled 
- ✅ Date and time leading to Select Time subsection
- ✅ Watermark image that leads to Upload Image subsection
- ✅ Text watermark: To receive the watermark text to be added to the cuts 
- ✅ Cutting seconds: To receive the time of each cut in seconds with a maximum of 460 seconds
- ✅ Subtitle Color: To receive the name of the color to be added to the cuts 
- ✅ selector_color_subtitles that leads to the Selector color subtitles subsection
- ✅ Subtitle Animation: To receive the name of the title animation to be added to the cuts 
- ✅ selector_animation_subtitles that leads to the Selector Animation Subtitles subsection
- ✅ Subtitle Effects: To receive the name of the title effect to be added to the cuts 
- ✅ selector_Effects_subtitles that leads to the Selector Effects Subtitles subsection
- ✅ Subtitle FontName: To receive the title font name to be added to the cuts 
- ✅ selector_FontName_subtitles that leads to the Selector FontName Subtitles subsection
- ✅ Captions Alignment: To receive the Caption Alignment to be added to the cuts (By Default 3)
- ✅ Captions Fontsize: To receive the Captions Font Size to be added to the cuts (By Default 8)
- ✅ Captions Primary Color: To receive the primary color of the caption to be added to the cuts 
- ✅ selector_PrimaryColour_Captions that leads to the Selector Primary Color Captions subsection
- ✅ Captions Secondary Color: To receive the secondary color of the caption to be added to the cuts 
- ✅ selector_SecondaryColour_Captions that leads to the Selector Secondary Color Captions subsection
- ✅ Captions Outline Color: To receive the caption outline color to be added to the cuts 
- ✅ selector_SecondaryColour_Captions that leads to the Selector Outline Color Captions subsection
- ✅ Captions Back Color: To receive the back color of the subtitles to be added to the cuts 
- ✅ selector_SecondaryColour_Captions that leads to the Selector Back Color Captions subsection
- ✅ Captions Bold: To receive a decision if the user wants the caption to be in bold (Enabled by Default)
- ✅ Captions Shadow: To receive a decision if the user wants the caption to have Shadow (Enabled by Default)
- ✅ Captions Italic: To receive a decision if the user wants the caption to be in italics
- ✅ Captions Underline: To receive a decision if the user wants the caption to be Underlined
- ✅ Captions Outline: To receive the Outline size of the captions
- ✅ Captions Reveal Effect Initial Color: To receive the primary color of the subtitles reveal effect
- ✅ selector_Reveal_Effect_Initial_Color_Captions which leads to the Selector Reveal Effect Initial Color Captions subsection
- ✅ Captions Reveal Effect Final Color: To receive the secondary color of the subtitle reveal effect
- ✅ selector_Reveal_Effect_Final_Color_Captions which leads to the Selector Reveal Effect Final Color Captions subsection

###### Subsections
- ✅ Select Time subsection: Receives the days of the week and scheduling time of the task, option of 2 modes, the first being week mode that uses the day and time provided and through a checkbox the user selects whether they want it to be executed throughout the month on the specified day of the week and time or if they prefer it to run indefinitely until the task is deleted, the second mode is the specific date that the user provides year month day date time where the task will be executed 
- ✅ Upload Image subsection receives the user's watermark image
- ✅ Upload Image subsection Preview of the uploaded image 
- ✅ Selector color subtitles subsection User has an advanced color picker similar to Google Color Picker
- ✅ Selector Animation Subtitles subsection
- ✅
-
###### Mode Batch processing
- []
###### Mode 1 long video
- []


##### QWebhook - Get processes
- ✅ Receiving Webhook log
- ✅ Receiving Weather Forecast from Webhook
- ✅ Receiving Cuts Duration from Webhook
- ✅ Receiving Webhook Messages
- ✅ Receiving Webhook base media
- ✅ Receiving target from Webhook
- ✅ Receiving created at from Webhook
- ✅ Receiving Webhook thread
- ✅ Receiving progress in % of the Webhook
- [] Receiving filepath from Webhook

##### QWebhook Slots
- ✅ Log signal Connected
- ✅ Weather Forecast signal Connected
- ✅ Cuts Duration signal Connected
- ✅ Messages signal Connected
- ✅ media base signal Connected
- ✅ Connected target signal
- ✅ created at signal Connected
- ✅ Connected thread signal
- ✅ Connected progress signal
- [] filepath signal Connected

##### Account info
- ✅ The user's full email is loaded in "Email:"
- ✅ User's API Key is loaded in "API Key:"
- ✅ Available API Server is loaded in "API Server:"
- ✅ License expiration of the user is loaded in "License expiration:"
- [] Notifications for the user to control whether they want to receive notifications on Windows about processes
