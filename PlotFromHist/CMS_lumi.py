from ROOT import *

cmsText     = "CMS";
cmsTextFont   = 61;  # default is helvetic-bold

writeExtraText = False;
isPreliminary = False;
extraText   = "Preliminary";
extraTextFont = 52;  # default is helvetica-italics

writeChannelText = False
channelText     = "";
channelTextFont   = 42;  # default is helvetic
channelTextLocation = -1 #1 left, 2 center, 3 right, -1 is same as other text

# text sizes and text offsets with respect to the top frame
# in unit of the top margin size
lumiTextSize     = 0.6;
lumiTextOffset   = 0.2;
cmsTextSize      = 0.75;
cmsTextOffset    = 0.1;  # only used in outOfFrame version

relPosX    = 0.045;
relPosY    = 0.035;
relExtraDY = 1.2;

# ratio of "CMS" and extra text size
extraOverCmsTextSize  = 0.76;

lumi_13TeV = "35.8 fb^{-1}";
lumi_8TeV  = "19.7 fb^{-1}";
lumi_7TeV  = "5.1 fb^{-1}";
lumi_sqrtS = "";

drawLogo      = False;

# second parameter in example_plot is iPos, which drives the position of the CMS logo in the plot
# iPos=11 : top-left, left-aligned
# iPos=33 : top-right, right-aligned
# iPos=22 : center, centered
# mode generally : 
#   iPos = 10*(alignement 1/2/3) + position (1/2/3 = left/center/right)

def CMS_lumi( pad, iPeriod, iPosX, extraLumiText = "" ):
    outOfFrame    = False;
    if iPosX/10==0 :
        outOfFrame = True;
    alignY_=3;
    alignX_=2;
    if iPosX/10==0: alignX_=1;
    if iPosX==0   : alignX_=1;
    if iPosX==0   : alignY_=1;
    if iPosX/10==1: alignX_=1;
    if iPosX/10==2: alignX_=2;
    if iPosX/10==3: alignX_=3;
    align_ = 10*alignX_ + alignY_;
    
    H = pad.GetWh();
    W = pad.GetWw();
    l = pad.GetLeftMargin();
    t = pad.GetTopMargin();
    r = pad.GetRightMargin();
    b = pad.GetBottomMargin();

    pad.cd();

    lumiText = ""
    if iPeriod==1:
        lumiText += lumi_7TeV;
        lumiText += " (7 TeV)";
    elif iPeriod==2:
        lumiText += lumi_8TeV;
        lumiText += " (8 TeV)";
    elif iPeriod==3:
        lumiText = lumi_8TeV; 
        lumiText += " (8 TeV)";
        lumiText += " + ";
        lumiText += lumi_7TeV;
        lumiText += " (7 TeV)";
    elif iPeriod==4:
        lumiText += lumi_13TeV;
        lumiText += " (13 TeV)";
    elif iPeriod==7:
        if outOfFrame : lumiText += "#scale[0.85]{";
        lumiText += lumi_13TeV; 
        lumiText += " (13 TeV)";
        lumiText += " + ";
        lumiText += lumi_8TeV; 
        lumiText += " (8 TeV)";
        lumiText += " + ";
        lumiText += lumi_7TeV;
        lumiText += " (7 TeV)";
        if outOfFrame: lumiText += "}";
    elif iPeriod==12:
        lumiText += "8 TeV";
    elif iPeriod==0:
        lumiText += lumi_sqrtS;

    if not extraLumiText =="":
        if not extraLumiText[0] == " ":
            extraLumiText = " " + extraLumiText
        lumiText += extraLumiText
   
    # print lumiText

    latex = TLatex()
    latex.SetNDC();
    latex.SetTextAngle(0);
    latex.SetTextColor(kBlack);    
    
    extraTextSize = extraOverCmsTextSize*cmsTextSize;

    latex.SetTextFont(42);
    latex.SetTextAlign(31); 
    latex.SetTextSize(lumiTextSize*t);    
    latex.DrawLatex(1-r,1-t+lumiTextOffset*t,lumiText);

    if outOfFrame:
        latex.SetTextFont(cmsTextFont);
        latex.SetTextAlign(11); 
        latex.SetTextSize(cmsTextSize*t);    
        latex.DrawLatex(l,1-t+lumiTextOffset*t,cmsText);
  
    pad.cd();

    posX_=0;
    l_pos = l + relPosX*(1-l-r);
    c_pos = l + 0.5*(1-l-r);
    r_pos = 1-r - relPosX*(1-l-r);
    if iPosX%10<=1:
        posX_ =   l_pos;
    elif iPosX%10==2:
        posX_ =  c_pos;
    elif iPosX%10==3:
        posX_ =  r_pos;

    posY_ = 1-t - relPosY*(1-t-b);
    
    ChanposX = l_pos
    channelalign = 11
    if channelTextLocation == 1:
        ChanposX = l_pos
        channelalign = 11
    elif channelTextLocation == 2:
        ChanposX = c_pos
        channelalign = 22
    elif channelTextLocation == 3:
        ChanposX = r_pos
        channelalign = 33
    elif channelTextLocation == -1:
        ChanposX = posX_
        channelalign = align_

    ChanposY = posY_
    if ChanposX==posX_:
        ChanposY = posY_-relExtraDY*(cmsTextSize)*t

        if writeExtraText:
#            ChanposY = posY_-2.15*relExtraDY*(cmsTextSize)*t
            ChanposY = posY_-relExtraDY*(cmsTextSize+extraTextSize)*t
            

    if not outOfFrame :
        if drawLogo:
            posX_ =   l + 0.045*(1-l-r)*W/H;
            posY_ = 1-t - 0.045*(1-t-b);
            xl_0 = posX_;
            yl_0 = posY_ - 0.15;
            xl_1 = posX_ + 0.15*H/W;
            yl_1 = posY_;
            CMS_logo = TASImage("CMS-BW-label.png");
            pad_logo = TPad("logo","logo", xl_0, yl_0, xl_1, yl_1 );
            pad_logo.Draw();
            pad_logo.cd();
            CMS_logo.Draw("X");
            pad_logo.Modified();
            pad.cd();
        else:
            latex.SetTextFont(cmsTextFont);
            latex.SetTextSize(cmsTextSize*t);
            latex.SetTextAlign(align_);
            latex.DrawLatex(posX_, posY_, cmsText);
            if writeExtraText: 
                latex.SetTextFont(extraTextFont);
                latex.SetTextAlign(align_);
                latex.SetTextSize(extraTextSize*t);
                latex.DrawLatex(posX_, posY_- relExtraDY*cmsTextSize*t, extraText);
            if writeChannelText:
                latex.SetTextFont(channelTextFont);
                latex.SetTextAlign(channelalign);
                latex.SetTextSize(extraTextSize*t);
                latex.DrawLatex(ChanposX, ChanposY, channelText);
                # if isPreliminary:
#                     latex.DrawLatex(posX_, posY_- relExtraDY*cmsTextSize*t, "#splitline{Preliminary}{%s}"%extraText);
#                 else:
    elif writeExtraText :
        if iPosX==0:
            posX_ =   l +  relPosX*(1-l-r);
            posY_ =   1-t+lumiTextOffset*t;
        latex.SetTextFont(extraTextFont);
        latex.SetTextSize(extraTextSize*t);
        latex.SetTextAlign(align_);
        latex.DrawLatex(posX_, posY_, extraText);      
    return pad
