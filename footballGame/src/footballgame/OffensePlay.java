/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package footballgame;
import java.util.*;
import java.lang.Math;
/**
 *
 * @author chrismoroney
 */
public class OffensePlay {
    Team teamOFF;
    Team teamDEF;
    
    Boolean isFirstDown = false;
    Boolean isTouchDown = false;
    
    // values tentative
    int yardsToDown = 10; 
    int yardsToTD = 75;
    
    public void runPlay(){
        if (isFirstDown){
            yardsToDown = 10;
        }    
        int probOFF = (teamOFF.OLINE + teamOFF.RB) / 2;
        int probDEF = (teamDEF.DLINE + teamDEF.LB1 + teamDEF.LB2) / 3;
        
        Random random = new Random();
        int probDistance = random.nextInt(100) + 1;
        int distance;
        // ranges for runs
        // 75-100 -> 2%
        // 50-74 -> 5%
        // 25-49 -> 13%
        // 10-24 -> 20%
        // -5-9 -> 60%
        if (1 <= probDistance && probDistance < 3 + Math.abs(probOFF - probDEF)){
            distance = random.nextInt(25) + 75;
        } else if (3 <= probDistance && probDistance < 7 + Math.abs(probOFF - probDEF)){
            distance = random.nextInt(24) + 50;
        } else if (7 <= probDistance && probDistance < 20 + Math.abs(probOFF - probDEF)){
            distance = random.nextInt(24) + 25;
        } else if (20 <= probDistance && probDistance < 40 + Math.abs(probOFF - probDEF)){
            distance = random.nextInt(14) + 10;
        } else {
            distance = random.nextInt(14) - 5;
        }
        yardsToTD -= distance;
        yardsToDown -= distance;
        if (yardsToTD <= 0){
            isTouchDown = true;
        } else if (yardsToDown <= 0){
            isFirstDown = true;
        } else {
            
        }
    }
    
    public void shortPass(){
        if (isFirstDown){
            yardsToDown = 10;
        } 
        
        Random random = new Random();
        int passToWR1 = random.nextInt(100) + 5;
        int passToWR2 = random.nextInt(100) + 20;
        int passToTE = random.nextInt(100) + 10;
        int passToRB = random.nextInt(100) + 5;
        
        int pass = Math.max(passToWR1, Math.max(passToWR2, Math.max(passToTE, passToRB)));
        double probOFF, probDEF;
        
        if (pass == passToWR1){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.WR1) / 2);
            probDEF = ((0.5 * teamDEF.FS) + teamDEF.CB1) / 2;
        } else if (pass == passToWR2){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.WR2) / 2);
            probDEF = ((0.5 * teamDEF.SS) + teamDEF.CB2) / 2;
        } else if (pass == passToTE){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.TE) / 2);
            probDEF = ((0.5 * teamDEF.SS) + teamDEF.LB2) / 2;
        } else {
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.RB) / 2);
            probDEF = ((0.5 * teamDEF.FS) + teamDEF.LB1) / 2;
        }
        
        if (probOFF >= probDEF){
            // Complete
        } else {
            // Incomplete
        }
    }
    
    public void longPass(){
        if (isFirstDown){
            yardsToDown = 10;
        } 
        
        Random random = new Random();
        int passToWR1 = random.nextInt(100) + 20;
        int passToWR2 = random.nextInt(100) + 8;
        int passToTE = random.nextInt(100) + 15;
        int passToRB = random.nextInt(100) + 1;
        
        int pass = Math.max(passToWR1, Math.max(passToWR2, Math.max(passToTE, passToRB)));
        double probOFF, probDEF;
        
        if (pass == passToWR1){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.WR1) / 2);
            probDEF = ((0.5 * teamDEF.FS) + teamDEF.CB1) / 2;
        } else if (pass == passToWR2){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.WR2) / 2);
            probDEF = ((0.5 * teamDEF.SS) + teamDEF.CB2) / 2;
        } else if (pass == passToTE){
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.TE) / 2);
            probDEF = ((0.5 * teamDEF.SS) + teamDEF.LB2) / 2;
        } else {
            probOFF = ((0.8 * teamOFF.QB + 0.8 * teamOFF.RB) / 2);
            probDEF = ((0.5 * teamDEF.FS) + teamDEF.LB1) / 2;
        }
        
        if (probOFF >= probDEF){
            // Complete
        } else {
            // Incomplete
        }
    }
}
