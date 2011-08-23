#!/usr/bin/env python
# encoding: utf-8
"""
plottingstuff.py

Created by Bryn Mathias on 2011-08-22.
Copyright (c) 2011 Imperial College. All rights reserved.
"""

import sys
import os
import ROOT as r


leg = r.TLegend(0.1, 0.4, 0.6, 1.0)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.SetShadowColor(0)
leg.SetBorderSize(0)
leg.SetFillStyle(4100)
leg.SetFillColor(0)
leg.SetLineColor(0)
closeList= []
def GetHist(DataSetName = "TFile.root",folder = None ,hist = "myHist",col = 0,norm = None ,Legend = "hist", rebin = None):
    if "root" in  DataSetName:
      a = r.TFile.Open(DataSetName) #open the file
    else:
      a = DataSetName
    # print a
    # closeList.append(a) # append the file to the close list
    if folder != None:
      b = a.Get(folder) #open the directory in the root file
      Hist = b.Get(hist)
    else:
      Hist = a.Get(hist) # get your histogram by name
    if Hist == None : Hist = r.TH1D()
    if Legend != 0:
      leg.AddEntry(Hist,Legend,"LP") # add a legend entry
    Hist.SetLineWidth(3)
    Hist.SetLineColor(col) #set colour
    if norm != None:
       Hist.Scale(norm) #if not data normilse to the data by lumi, MC is by default weighted to 100pb-1, if you have changed this change here!
    if rebin != None:
       Hist.Rebin2D(rebin,rebin)
    return Hist


def Adder(hist):
  out = None
  tot = 0
  for h in hist:
    tot += h.GetBinContent(62,36)
    print "Totting up"  ,tot
    if out == None: out = h.Clone()
    else: out.Add(h)
  """docstring for Adder"""
  return out
  pass

def weightedAdder(hist,weight):
  if len(hist) != len(weight): print "Weight list and hist list are not the same lenght"
  out = None
  for h,w in zip(hist,weight):
    if out == None:
      out = h.Clone()
      out.Multiply(w)
    else :
      h.Multiply(w)
      out.Add(h)
  return out
  pass

def nloTotalXsecMaker(weighted,notweighted):
  """Take two sets of histograms and make the NLO total cross section from it"""
  out = None
  nom = Adder(weighted)
  denom = Adder(notweighted)
  print "no events per bin:", denom.GetBinContent(62,36)
  out = nom.Clone()
  out.Divide(denom)
  return out


def NloEffHisto(aftercuts,beforecuts,TotalXsec):
  """Make CMSSM NLO plots from input histograms"""
  out = None
  for after,before in zip(aftercuts,beforecuts):
      h = after.Clone()
      h.Divide(before)
      if out is None: out = h.Clone()
      else:           out.Add(h)
  out.Divide(TotalXsec)
  return out
  pass




# def rebinScan(Hist):
#   """docstring for rebinScan"""
#   # find lowest bin
#   for bin in range(Hist.GetNBinsX())
#     if Hist.GetBinContent(bin) != 0:
#       low = Hist.GetBinLowEdge(bin - 100)
#       break
#   def HistogramMaxX(H):
#   Nbins = H.GetNbinsX()
#   BackItr = range(0,Nbins)
#   BackItr.reverse()
#   for x in BackItr :
#     if H.GetBinContent(x) != 0:
#       return H.GetBinLowEdge(x+1)
#   pass