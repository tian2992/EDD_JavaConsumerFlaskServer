import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import org.json.*;

public class TestClass {

	public static void main(String[] args) throws IOException {
		


		OkHttpClient cliente = new OkHttpClient();

		//URL url = new URL("http://localhost:5000/aviones/");
		URL url = new URL("http://localhost:5000/aviones/agregar");
		
		RequestBody formBody = new FormEncodingBuilder()
        .add("message", "Hola, es una prueba de EDD")
        .build();

		
		Request request = new Request.Builder()
			.url(url)
			.post(formBody)
			.build();

		Response response = cliente.newCall(request).execute();

		String response_string = response.body().string();
		System.out.println(response_string);
	
		JSONArray array_de_objetos = new JSONArray(response_string);
		for (int i = 0; i < array_de_objetos.length(); i++) {
			JSONObject avion = array_de_objetos.getJSONObject(i);
			System.out.println("nombre: " + avion.get("nombre"));
			System.out.println("id: " + avion.get("id"));
			
		}


	}
}
