module.exports = {
  devtool: "inline-source-map",
  entry: "./app.py",
  mode: "development",
  module: {
    rules: [
      {
        test: /\.py$/,
        loader: "transcrypt-loader",
        options: {},
      },
    ],
  },
};
