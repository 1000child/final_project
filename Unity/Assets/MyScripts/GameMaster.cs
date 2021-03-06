using UnityEngine;
using System.Collections;


public class GameMaster : MonoBehaviour {

	public static GameMaster gm;

	void Awake () {
		if (gm == null) {
			gm = GameObject.FindGameObjectWithTag ("GM").GetComponent<GameMaster>();
		}
	}

	public Transform playerPrefab;
	public Transform spawnPoint;
	public float spawnDelay = 2;
	public Transform spawnPrefab;


	public IEnumerator _RespawnPlayer () {
		GetComponent<AudioSource>().Play ();
		yield return new WaitForSeconds (spawnDelay);

		Instantiate (playerPrefab, spawnPoint.position, spawnPoint.rotation);

	}

	public static void KillPlayer (Player player) {
		Destroy (player.gameObject);
		gm.StartCoroutine(gm._RespawnPlayer());
	}

	public static void KillEnemy (Enemy enemy) {
		gm._KillEnemy(enemy);
	}
	public void _KillEnemy(Enemy _enemy)
	{
		Destroy(_enemy.gameObject);
	}

}
