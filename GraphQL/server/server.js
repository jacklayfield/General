const express = require("express");
const { graphqlHTTP } = require("express-graphql");
const { buildSchema } = require("graphql");
const mongoose = require("mongoose");
const cors = require("cors");
require("dotenv").config();

mongoose.connect(process.env.MONGO_URI, {});

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

// Define GraphQL resolvers
const root = {
  posts: async () => await Post.find(),
  post: async ({ id }) => await Post.findById(id),
  createPost: async ({ input }) => {
    const post = new Post(input);
    await post.save();
    return post;
  },
  updatePost: async ({ id, input }) => {
    await Post.findByIdAndUpdate(id, input);
    return await Post.findById(id);
  },
  deletePost: async ({ id }) => await Post.findByIdAndDelete(id),
};

const app = express();

app.use(cors());

// Define GraphQL endpoint
app.use(
  "/graphql",
  graphqlHTTP({
    schema,
    rootValue: root,
    graphiql: true,
  })
);

const PORT = process.env.PORT || 4000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
