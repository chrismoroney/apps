/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package footballgame;

/**
 *
 * @author chrismoroney
 */
public class Team {
    int QB;
    int RB;
    int WR1;
    int WR2;
    int TE;
    int OLINE;
    double OFF_AVERAGE;
    
    int DLINE;
    int LB1;
    int LB2;
    int CB1;
    int CB2;
    int FS;
    int SS;
    double DEF_AVERAGE;
    
    int PUNT;
    int KICK;
    
    int COACH;
    boolean HOME_STADIUM;
     
    public Team() {
        this.QB = 30;
        this.RB = 30;
        this.WR1 = 30;
        this.WR2 = 30;
        this.TE = 30;
        this.OLINE = 30;

        this.DLINE = 30;
        this.LB1 = 30;
        this.LB2 = 30;
        this.CB1 = 30;
        this.CB2 = 30;
        this.FS = 30;
        this.SS = 30;
        
        this.PUNT = 30;
        this.KICK = 30;
        
        this.COACH = 30;
    }
    
    public double get_OFF_AVERAGE(){
        return calc_OFF_AVERAGE();
    }
    
    private double calc_OFF_AVERAGE(){
        return (QB + RB + WR1 + WR2 + TE + OLINE + (COACH * 0.5)) / 6;
    }
    
    public double get_DEF_AVERAGE(){
        return calc_DEF_AVERAGE();
    }
    
    private double calc_DEF_AVERAGE(){
        return (DLINE + LB1 + LB2 + CB1 + CB2 + FS + SS + (COACH * 0.5)) / 6;
    }
    
    public void setQB(int newQB) {
        this.QB = newQB;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getQB(){
        return this.QB;
    }
    
    public void setRB(int newRB) {
        this.QB = newRB;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getRB(){
        return this.RB;
    }
    
    public void setWR1(int newWR1) {
        this.QB = newWR1;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getWR1(){
        return this.WR1;
    }
    
    public void setWR2(int newWR2) {
        this.QB = newWR2;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getWR2(){
        return this.WR2;
    }
    
    public void setTE(int newTE) {
        this.QB = newTE;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getTE(){
        return this.TE;
    }
    
    public void setOLINE(int newOLINE) {
        this.QB = newOLINE;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getOLINE(){
        return this.OLINE;
    }
    
    public void setDLINE(int newDLINE) {
        this.QB = newDLINE;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getDLINE(){
        return this.DLINE;
    }
    
    public void setLB1(int newLB1) {
        this.QB = newLB1;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getLB1(){
        return this.LB1;
    }
    
    public void setLB2(int newLB2) {
        this.QB = newLB2;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getLB2(){
        return this.LB2;
    }
    
    public void setCB1(int newCB1) {
        this.QB = newCB1;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getCB1(){
        return this.CB1;
    }
    
    public void setCB2(int newCB2) {
        this.QB = newCB2;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getCB2(){
        return this.CB2;
    }
    
    public void setFS(int newFS) {
        this.QB = newFS;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getFS(){
        return this.FS;
    }
    
    public void setSS(int newSS) {
        this.QB = newSS;
        this.OFF_AVERAGE = calc_OFF_AVERAGE();
    }
    public int getSS(){
        return this.SS;
    }
}
