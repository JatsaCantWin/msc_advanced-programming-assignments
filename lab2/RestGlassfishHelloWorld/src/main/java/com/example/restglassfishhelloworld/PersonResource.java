package com.example.restglassfishhelloworld;

import jakarta.ws.rs.*;
import jakarta.ws.rs.core.MediaType;

@Path("/person")
public class PersonResource {
    public static class Person {
        public String name;
        public int age;

        public String toString() {
            return name + " " + age;
        }
    }

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Person getPerson()
    {
        Person person = new Person();
        person.age = 32;
        person.name = "Oleg";
        return person;
    }

    @POST
    @Produces(MediaType.TEXT_PLAIN)
    @Consumes(MediaType.APPLICATION_JSON)
    public String handlePersonRequest(Person person) {
        return person.toString();
    }
}

