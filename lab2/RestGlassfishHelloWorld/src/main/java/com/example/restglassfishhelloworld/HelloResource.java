package com.example.restglassfishhelloworld;

import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;

@Path("/hello-world")
public class HelloResource {
    @GET
    @Produces("text/plain")
    public String hello() {
        return "Hello, World!";
    }

    @Path("/{name}")
    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String doGreeting(@PathParam("name") String someValue, @QueryParam("language") String language) {
        return "Hello " + someValue + " with language " + language;
    }
}

