const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const mongoose = require("mongoose");
const cors = require("cors");

mongoose.connect("mongodb://localhost/graphql-blog", {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const Post = mongoose.model("Post", { title: String, content: String });

// GraphQL schema
const schema = buildSchema(`
  type Post {
    id: ID!
    title: String!
    content: String!
  }

  input PostInput {
    title: String!
    content: String!
  }

  type Query {
    posts: [Post]
    post(id: ID!): Post
  }

  type Mutation {
    createPost(input: PostInput!): Post
    updatePost(id: ID!, input: PostInput!): Post
    deletePost(id: ID!): Post
  }
`);
