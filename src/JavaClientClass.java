/*
 * A small program to consume REST services using OkHTTP and JSON.
 * Author: Sebastian Oliva (200815609@ingenieria.usac.edu.gt)
 */

import java.io.IOException;
import java.net.URL;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import org.json.*;

public class JavaClientClass {

	public static OkHttpClient webClient = new OkHttpClient();

	public static void printPlanes() throws IOException {
		URL url = new URL("http://localhost:5000/aviones/");
		Request request = new Request.Builder().url(url).build();

		Response response = webClient.newCall(request).execute();
		String response_string = response.body().string();

		JSONArray objects_array = new JSONArray(response_string);
		for (int i = 0; i < objects_array.length(); i++) {
			JSONObject avion = objects_array.getJSONObject(i);
			System.out.println("name: " + avion.get("name"));
			System.out.println("id: " + avion.get("id"));
		}
	}

	public static void addPlane() throws IOException {
		URL url = new URL("http://localhost:5000/aviones/agregar");

		RequestBody formBody = new FormEncodingBuilder()
				.add("name", "MyJavaPlane")
				.add("model", "Coffee-7-Model")
				.build();

		Request request = new Request.Builder().url(url).post(formBody).build();

		Response response = webClient.newCall(request).execute();
		String response_string = response.body().string();
		System.out.println(response_string);
	}

	public static void main(String[] args) throws IOException {
		printPlanes();
		addPlane();
		printPlanes();
	}
}
