module.exports = async function (context, req) {
  context.res = {
    // status: 200, /* Defaultss to 200 */
    body: { text: "Hellsloss from the APIs" },
  };
};
