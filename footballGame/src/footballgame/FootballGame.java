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
public class FootballGame {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Team team1 = new Team();
        System.out.println(team1.getQB());
        team1.setQB(40);
        System.out.println(team1.getQB());
        
        System.out.println(team1.get_OFF_AVERAGE());
    }
    
}
