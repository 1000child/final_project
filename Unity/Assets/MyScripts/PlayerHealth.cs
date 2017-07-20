using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerHealth : MonoBehaviour {

    public class PlayerStats
    {
        public int maxHealth = 100;

        private int _curHealth;
        public int curHealth
        {
            get { return _curHealth; }
            set { _curHealth = Mathf.Clamp(value, 0, maxHealth); }
        }

        public void Init()
        {
            curHealth = maxHealth;
        }
    }

    public static void CaughtPlayer(PlayerHealth player)
    { 
        Destroy(player.gameObject);
    }

    public PlayerStats stats = new PlayerStats();

    public void DamagePlayer(int damage)
    {
        stats.curHealth -= damage;
        if (stats.curHealth <= 0)
        {
            CaughtPlayer(this);
        }
    }

    public int wordDamage = -25;

    void Update()
    {
     //if (touches words) {
      //    (DamagePlayer (Mathf.wordDamage)
    }

}
